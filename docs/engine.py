# Arcade engine. The play page runs this in the browser.
# It plays a game until the game calls input(), then hands that
# question back to the page. screen.textinput() waits the same way.
# Turtle drawings are sent back for the page to paint.
# You do not run this file yourself.

import builtins
import json
import math
import os
import random
import sys
import traceback
import types
from io import StringIO

if "USER_SOURCE" not in globals():
    raise SystemExit(
        "This file is the arcade engine. Open docs/index.html through a local server instead."
    )


class NeedInput(Exception):
    def __init__(self, prompt):
        super().__init__(prompt)
        self.prompt = prompt


class _Capped(StringIO):
    def write(self, text):
        if self.tell() > 120000:
            raise RuntimeError(
                "Stopped this run because it printed too much. Try smaller numbers."
            )
        return super().write(text)


class _LineLimit:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __call__(self, frame, event, arg):
        if event == "line":
            self.count += 1
            if self.count > self.limit:
                raise RuntimeError(
                    "Stopped this run because it went on too long. "
                    "If you typed a huge number, try a smaller one. "
                    "If a loop never ends, it needs a way to stop."
                )
        return self


parsed_answers = json.loads(USER_ANSWERS_JSON)
if not isinstance(parsed_answers, list):
    parsed_answers = []
answers = ["" if item is None else str(item) for item in parsed_answers[:1000]]
seed = int(USER_SEED)
step_limit = int(globals().get("USER_STEP_LIMIT", 500000))
filename = str(globals().get("USER_FILENAME") or "game.py")
filename = filename.replace("\\", "/").split("/")[-1] or "game.py"
source = USER_SOURCE if isinstance(USER_SOURCE, str) else str(USER_SOURCE)

random.seed(seed)

if os.path.isdir("/home/pyodide"):
    os.chdir("/home/pyodide")

captured_out = _Capped()
captured_err = StringIO()
old_out = sys.stdout
old_err = sys.stderr
old_input = builtins.input
sys.stdout = captured_out
sys.stderr = captured_err

index = 0


def arcade_input(prompt=""):
    global index
    if prompt is None:
        prompt = ""
    else:
        prompt = str(prompt)
    if index >= len(answers):
        raise NeedInput(prompt)
    answer = answers[index]
    index += 1
    sys.stdout.write(prompt)
    sys.stdout.write(answer + "\n")
    return answer


builtins.input = arcade_input

# Browser stand-in for Python's turtle module. The real one needs Tk,
# which the browser Python does not have. Same method names and movement
# rules; each move is recorded so the page can draw it.
turtle_state = {
    "used": False,
    "width": 400,
    "height": 300,
    "bg": "#ffffff",
    "lines": [],
    "frames": [],
}


def _install_turtle():
    screen_box = {"screen": None}

    def _color_name(value):
        if isinstance(value, str) and value:
            return value
        return "black"

    class Screen:
        def __new__(cls, *args, **kwargs):
            if screen_box["screen"] is None:
                screen_box["screen"] = object.__new__(cls)
                screen_box["screen"]._ready = False
            return screen_box["screen"]

        def __init__(self):
            if self._ready:
                return
            self._ready = True
            self._turtles = []
            turtle_state["used"] = True

        def setup(self, width=400, height=300, startx=None, starty=None):
            turtle_state["used"] = True
            turtle_state["width"] = _pixels(width, 400)
            turtle_state["height"] = _pixels(height, 300)

        def textinput(self, title, prompt):
            turtle_state["used"] = True
            message = "" if prompt is None else str(prompt)
            if message == "" and title:
                message = str(title)
            return arcade_input(message)

        def exitonclick(self):
            turtle_state["used"] = True
            return None

        def _snapshot(self):
            if not turtle_state["frames"]:
                turtle_state["output_before_motion"] = captured_out.getvalue()
            turtles = []
            for item in self._turtles:
                turtles.append(
                    {
                        "x": item._x,
                        "y": item._y,
                        "heading": item._heading,
                        "color": _color_name(item._pencolor),
                        "fill": _color_name(item._fillcolor),
                        "visible": bool(item._shown),
                    }
                )
            frame = {"turtles": turtles, "lineCount": len(turtle_state["lines"])}
            frames = turtle_state["frames"]
            if len(frames) < 4000:
                frames.append(frame)
            elif frames:
                frames[-1] = frame

    class Turtle:
        def __init__(self, shape="classic", undobuffersize=1000, visible=True):
            self._screen = Screen()
            self._x = 0.0
            self._y = 0.0
            self._heading = 0.0
            self._pencolor = "black"
            self._fillcolor = "black"
            self._pen = True
            self._shown = bool(visible)
            self._shape = shape or "classic"
            self._pensize = 1
            self._screen._turtles.append(self)
            turtle_state["used"] = True

        def color(self, *args):
            if not args:
                return (self._pencolor, self._fillcolor)
            if len(args) == 1:
                self._pencolor = args[0]
                self._fillcolor = args[0]
            else:
                self._pencolor = args[0]
                self._fillcolor = args[1]

        def pencolor(self, *args):
            if not args:
                return self._pencolor
            self._pencolor = args[0]

        def penup(self):
            self._pen = False

        def goto(self, x, y=None):
            if y is None and isinstance(x, (tuple, list)) and len(x) == 2:
                x, y = x
            self._move_to(float(x), float(y))

        def forward(self, distance):
            distance = float(distance)
            radians = math.radians(self._heading)
            self._move_to(
                self._x + distance * math.cos(radians),
                self._y + distance * math.sin(radians),
            )

        def xcor(self):
            return self._x

        def _move_to(self, x, y):
            if self._pen and (x != self._x or y != self._y):
                turtle_state["lines"].append(
                    {
                        "x1": self._x,
                        "y1": self._y,
                        "x2": x,
                        "y2": y,
                        "color": _color_name(self._pencolor),
                        "width": self._pensize,
                    }
                )
            self._x = x
            self._y = y
            self._screen._snapshot()

    def _pixels(value, default):
        try:
            number = float(value)
        except (TypeError, ValueError):
            return default
        if number <= 1:
            return default
        return int(number)

    module = types.ModuleType("turtle")
    module.Turtle = Turtle
    module.Screen = Screen
    module.__file__ = "turtle.py"
    sys.modules["turtle"] = module


_install_turtle()

status = "done"
prompt_out = ""
error_out = ""
limiter = _LineLimit(step_limit)
sys.settrace(limiter)
try:
    code = compile(source, filename, "exec")
    namespace = {"__name__": "__main__", "__file__": filename}
    exec(code, namespace)
except NeedInput as needed:
    status = "need_input"
    prompt_out = needed.prompt
except SystemExit as exited:
    code_num = exited.code
    if code_num not in (None, 0):
        status = "error"
        error_out = "The program stopped early (SystemExit: %s)." % (code_num,)
except Exception as exc:
    status = "error"
    if isinstance(exc, RuntimeError) and str(exc).startswith("Stopped this run"):
        error_out = str(exc)
    else:
        raw = traceback.format_exc()
        skip = ("engine.py", "<exec>", "<string>", "arcade_input")
        kept = [
            line for line in raw.splitlines(True)
            if not any(marker in line for marker in skip)
        ]
        error_out = "".join(kept).strip() or str(exc)
finally:
    sys.settrace(None)
    sys.stdout = old_out
    sys.stderr = old_err
    builtins.input = old_input

extra_err = captured_err.getvalue().strip()
if extra_err and not error_out:
    error_out = extra_err

result_payload = {
    "status": status,
    "output": captured_out.getvalue(),
    "prompt": prompt_out,
    "error": error_out,
}
if turtle_state["used"]:
    result_payload["turtle"] = {
        "width": turtle_state["width"],
        "height": turtle_state["height"],
        "bg": turtle_state["bg"],
        "lines": turtle_state["lines"],
        "frames": turtle_state["frames"],
        "outputBeforeMotion": turtle_state.get("output_before_motion", ""),
    }

ARCADE_RESULT = json.dumps(result_payload)
ARCADE_RESULT

# Arcade engine. The play page runs this in the browser.
# It plays a game until the game calls input(), then hands that
# question back to the page. screen.textinput() asks after any turtles
# already on the screen have been drawn.
# Turtle drawings are sent back for the page to paint.
# screen.addshape() can load a .gif, and turtle.write() sends words
# back with the drawing.
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


def _wants_pandas(text):
    # Importing pandas walks a lot of Python. Do it before the step
    # limit starts, or the states game is stopped before it can ask.
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("import pandas") or stripped.startswith("from pandas "):
            return True
    return False


parsed_answers = json.loads(USER_ANSWERS_JSON)
if not isinstance(parsed_answers, list):
    parsed_answers = []
answers = ["" if item is None else str(item) for item in parsed_answers[:1000]]
seed = int(USER_SEED)
step_limit = int(globals().get("USER_STEP_LIMIT", 500000))
filename = str(globals().get("USER_FILENAME") or "game.py")
filename = filename.replace("\\", "/").split("/")[-1] or "game.py"
source = USER_SOURCE if isinstance(USER_SOURCE, str) else str(USER_SOURCE)

if _wants_pandas(source):
    try:
        import pandas
    except Exception:
        pass

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


def arcade_input(prompt="", echo=None):
    global index
    if prompt is None:
        prompt = ""
    else:
        prompt = str(prompt)
    # echo is what gets printed with the answer. input() leaves it
    # empty so the prompt is printed, same as before.
    if echo is None:
        echo_text = prompt
    else:
        echo_text = str(echo)
    if index >= len(answers):
        raise NeedInput(prompt)
    answer = answers[index]
    index += 1
    sys.stdout.write(echo_text)
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
    "labels": [],
    "frames": [],
    "shapes": {},
    "title": "",
}


def _gif_size(path):
    try:
        handle = open(path, "rb")
    except OSError:
        return None
    try:
        header = handle.read(10)
    finally:
        handle.close()
    if len(header) < 10 or header[:6] not in (b"GIF87a", b"GIF89a"):
        return None
    width = header[6] + (header[7] << 8)
    height = header[8] + (header[9] << 8)
    if width <= 0 or height <= 0:
        return None
    return width, height


def _font_css(font):
    if isinstance(font, str) and font:
        return font
    family = "Arial"
    size = 8
    style = ""
    weight = ""
    if isinstance(font, (tuple, list)):
        if len(font) >= 1 and font[0]:
            family = str(font[0])
        if len(font) >= 2:
            try:
                size = int(float(font[1]))
            except (TypeError, ValueError):
                size = 8
        if len(font) >= 3 and font[2]:
            extra = str(font[2]).lower()
            if "bold" in extra:
                weight = "bold"
            if "italic" in extra:
                style = "italic"
    parts = [part for part in (style, weight, "%spt" % size, family) if part]
    return " ".join(parts)


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
            self._setup_called = False
            turtle_state["used"] = True

        def setup(self, width=400, height=300, startx=None, starty=None):
            turtle_state["used"] = True
            self._setup_called = True
            turtle_state["width"] = _pixels(width, 400)
            turtle_state["height"] = _pixels(height, 300)

        def title(self, titlestring):
            turtle_state["used"] = True
            turtle_state["title"] = "" if titlestring is None else str(titlestring)

        def addshape(self, name, shape=None):
            turtle_state["used"] = True
            filename = "" if name is None else str(name)
            if shape is not None:
                turtle_state["shapes"][filename] = {"type": "polygon"}
                return None
            if not filename.lower().endswith(".gif"):
                raise RuntimeError("Turtle shapes loaded from a file have to be a .gif.")
            size = _gif_size(filename)
            if size is None:
                raise RuntimeError(
                    "Could not open the shape image %s. It needs to sit next to the program."
                    % (filename,)
                )
            turtle_state["shapes"][filename] = {
                "type": "image",
                "width": size[0],
                "height": size[1],
            }
            # The picture is the window. State coordinates are measured
            # from the middle of it, so the screen has to be that size
            # unless the program already chose one.
            if not self._setup_called:
                turtle_state["width"] = size[0]
                turtle_state["height"] = size[1]
            return None

        def textinput(self, title, prompt):
            turtle_state["used"] = True
            message = "" if prompt is None else str(prompt)
            if message == "" and title:
                message = str(title)
            # No answer yet. A blank bet is falsy, so the race stays off
            # while the turtles take their marks. The page asks after that.
            if index >= len(answers) and not turtle_state.get("deferred_textinput"):
                turtle_state["deferred_textinput"] = True
                turtle_state["awaiting_bet"] = True
                turtle_state["textinput_prompt"] = message
                return ""
            # A later question can carry the dialog title. That is where
            # the states game keeps the score. The opening question stays
            # prompt-only, and a typed answer is echoed with the prompt alone.
            title_text = "" if title is None else str(title)
            display = message
            if title_text and message and title_text not in message:
                display = title_text + "\n" + message
            return arcade_input(display, message)

        def exitonclick(self):
            turtle_state["used"] = True
            return None

        def _snapshot(self):
            if not turtle_state["frames"]:
                turtle_state["output_before_motion"] = captured_out.getvalue()
            turtles = []
            for item in self._turtles:
                shape_info = turtle_state["shapes"].get(item._shape, {})
                turtles.append(
                    {
                        "x": item._x,
                        "y": item._y,
                        "heading": item._heading,
                        "color": _color_name(item._pencolor),
                        "fill": _color_name(item._fillcolor),
                        "visible": bool(item._shown),
                        "shape": item._shape,
                        "image": shape_info.get("type") == "image",
                    }
                )
            frame = {
                "turtles": turtles,
                "lineCount": len(turtle_state["lines"]),
                "labelCount": len(turtle_state["labels"]),
            }
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

        def hideturtle(self):
            self._shown = False

        def showturtle(self):
            self._shown = True

        def shape(self, name=None):
            if name is None:
                return self._shape
            filename = str(name)
            builtin = ("classic", "turtle", "arrow", "circle", "square", "triangle")
            if filename not in turtle_state["shapes"] and filename not in builtin:
                raise RuntimeError("There is no shape named %s" % (filename,))
            self._shape = filename
            if turtle_state["shapes"].get(filename, {}).get("type") == "image":
                self._screen._snapshot()

        def write(self, arg, move=False, align="left", font=("Arial", 8, "normal")):
            text_align = align if align in ("left", "center", "right") else "left"
            turtle_state["labels"].append(
                {
                    "text": str(arg),
                    "x": self._x,
                    "y": self._y,
                    "align": text_align,
                    "color": _color_name(self._pencolor),
                    "font": _font_css(font),
                }
            )
            self._screen._snapshot()

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

    default_pen = {"pen": None}

    def _getpen():
        if default_pen["pen"] is None:
            default_pen["pen"] = Turtle()
        return default_pen["pen"]

    def shape(name=None):
        pen = _getpen()
        if name is None:
            return pen.shape()
        pen.shape(name)
        return None

    module = types.ModuleType("turtle")
    module.Turtle = Turtle
    module.Screen = Screen
    module.shape = shape
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

output_text = captured_out.getvalue()
if turtle_state.get("awaiting_bet") and status == "done":
    status = "need_input"
    prompt_out = turtle_state.get("textinput_prompt") or prompt_out
    if output_text.strip() == "":
        output_text = ""
    if turtle_state["frames"]:
        turtle_state["frames"] = [turtle_state["frames"][-1]]

result_payload = {
    "status": status,
    "output": output_text,
    "prompt": prompt_out,
    "error": error_out,
}
if turtle_state["used"]:
    result_payload["turtle"] = {
        "width": turtle_state["width"],
        "height": turtle_state["height"],
        "bg": turtle_state["bg"],
        "lines": turtle_state["lines"],
        "labels": turtle_state["labels"],
        "frames": turtle_state["frames"],
        "outputBeforeMotion": turtle_state.get("output_before_motion", ""),
        "title": turtle_state.get("title") or "",
    }

ARCADE_RESULT = json.dumps(result_payload)
ARCADE_RESULT

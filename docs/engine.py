# Arcade engine. The play page runs this in the browser.
# It plays a game until the game calls input(), then hands that
# question back to the page. You do not run this file yourself.

import builtins
import json
import os
import random
import sys
import traceback
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

ARCADE_RESULT = json.dumps(
    {
        "status": status,
        "output": captured_out.getvalue(),
        "prompt": prompt_out,
        "error": error_out,
    }
)
ARCADE_RESULT

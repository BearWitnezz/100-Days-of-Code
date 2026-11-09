"use strict";

const PYODIDE_BASE = "https://cdn.jsdelivr.net/pyodide/v0.28.3/full/";

const els = {
  kicker: document.getElementById("kicker"),
  title: document.getElementById("title"),
  description: document.getElementById("description"),
  howto: document.getElementById("howto"),
  filePath: document.getElementById("file-path"),
  pageError: document.getElementById("page-error"),
  fallback: document.getElementById("fallback"),
  fallbackReason: document.getElementById("fallback-reason"),
  fallbackLink: document.getElementById("fallback-link"),
  terminal: document.getElementById("terminal"),
  termTitle: document.getElementById("term-title"),
  termScroll: document.getElementById("term-scroll"),
  termOut: document.getElementById("term-out"),
  termPrompt: document.getElementById("term-prompt"),
  termError: document.getElementById("term-error"),
  termDone: document.getElementById("term-done"),
  turtleStage: document.getElementById("turtle-stage"),
  turtleCanvas: document.getElementById("turtle-canvas"),
  composer: document.getElementById("composer"),
  composerRow: document.getElementById("composer-row"),
  choices: document.getElementById("choices"),
  choiceTrue: document.getElementById("choice-true"),
  choiceFalse: document.getElementById("choice-false"),
  answer: document.getElementById("answer"),
  answerLabel: document.getElementById("answer-label"),
  go: document.getElementById("go"),
  hint: document.getElementById("hint"),
  undo: document.getElementById("undo"),
  restart: document.getElementById("restart"),
  toggleCode: document.getElementById("toggle-code"),
  codePanel: document.getElementById("code-panel"),
  codePicker: document.getElementById("code-picker"),
  codeName: document.getElementById("code-name"),
  copy: document.getElementById("copy"),
  codeText: document.getElementById("code-text"),
};

const HINTS = {
  loading: "First game takes a moment. Python is downloading.",
  running: "Running…",
  need_input: "Press Enter to send your answer.",
  true_false: "Press True or False.",
  done: "That's the whole program. Start over to run it again.",
  error: "Read the error, then undo the last answer or start over.",
  fallback: "Copy the code, then open the link and paste it in.",
};

let pyodidePromise = null;
let enginePromise = null;
let project = null;
let files = [];
let answers = [];
let seed = Math.floor(Math.random() * 1000000000) + 1;
let seedLocked = false;
let runId = 0;
let busy = false;
let turtlePlayback = 0;

const TURTLE_SHAPE = [
  [0, 16], [-2, 14], [-1, 10], [-4, 7], [-7, 9], [-9, 8], [-6, 5], [-7, 1],
  [-5, -3], [-8, -6], [-6, -8], [-4, -5], [0, -7], [4, -5], [6, -8], [8, -6],
  [5, -3], [7, 1], [6, 5], [9, 8], [7, 9], [4, 7], [1, 10], [2, 14],
];

const params = new URLSearchParams(location.search);
const seedParam = params.get("seed");
if (seedParam && /^\d+$/.test(seedParam)) {
  seed = Number(seedParam);
  seedLocked = true;
}

els.composer.addEventListener("submit", onSubmit);
els.choiceTrue.addEventListener("click", () => onChoice("True"));
els.choiceFalse.addEventListener("click", () => onChoice("False"));
els.restart.addEventListener("click", onRestart);
els.undo.addEventListener("click", onUndo);
els.toggleCode.addEventListener("click", onToggleCode);
els.copy.addEventListener("click", onCopy);
els.codePicker.addEventListener("change", showSelectedFile);
els.answer.addEventListener("focus", () => {
  els.answer.scrollIntoView({ block: "nearest" });
});

init();

async function init() {
  setStatus("loading");
  if (location.protocol === "file:") {
    fail("Open this site through a small local server. Double-clicking the HTML file will not load the games. The steps are in ADDING_A_GAME.md.");
    return;
  }
  const id = params.get("id");
  if (!id) {
    fail("Pick a game from the arcade homepage.");
    return;
  }
  try {
    const response = await fetch("projects.json", { cache: "no-cache" });
    if (!response.ok) throw new Error("Could not load projects.json (" + response.status + ").");
    const data = JSON.parse(await response.text());
    project = (data.projects || []).find((item) => item && item.id === id);
    if (!project) {
      fail("That game isn't in the list. Head back and pick another card.");
      return;
    }
    paintHeading();
    files = await loadFiles(project);
    showCode(false);
    if (project.playable === false) {
      showFallback();
      return;
    }
    await runGame(true);
  } catch (error) {
    const message = error instanceof SyntaxError
      ? "projects.json isn't valid JSON. Check commas and quotes. " + error.message
      : error.message;
    fail(message);
  }
}

function paintHeading() {
  if (typeof project.day === "number") document.body.dataset.day = String(project.day);
  else delete document.body.dataset.day;
  if (project.dayLabel) document.body.dataset.dayLabel = project.dayLabel;
  else delete document.body.dataset.dayLabel;
  els.kicker.textContent = project.badge || "";
  els.kicker.hidden = !project.badge;
  els.title.textContent = project.title;
  document.title = project.title + " · Plumber to Indie Developer Arcade";
  els.description.textContent = project.description || "";
  els.howto.textContent = project.howToPlay || "";
  const pretty = prettyPath(project.entry || "");
  els.filePath.textContent = "";
  if (pretty) {
    els.filePath.append("Running ");
    const code = document.createElement("code");
    code.textContent = pretty;
    els.filePath.append(code);
  }
  els.termTitle.textContent = baseName(project.entry || "game.py");
  document.body.dataset.project = project.id;
}

async function loadFiles(item) {
  if (!item.entry) throw new Error("This game has no entry file in projects.json.");
  const loaded = [{ name: baseName(item.entry), path: null, text: await loadText(item.entry) }];
  for (const file of item.files || []) {
    if (!file || !file.path || !file.src) {
      throw new Error("Each extra file needs a path and a src.");
    }
    if (file.path.startsWith("/") || file.path.includes("..")) {
      throw new Error("File path should look like words.py, not " + file.path);
    }
    loaded.push({ name: file.path, path: file.path, text: await loadText(file.src) });
  }
  return loaded;
}

function showFallback() {
  setStatus("fallback");
  els.terminal.hidden = true;
  els.restart.hidden = true;
  els.undo.hidden = true;
  els.composer.hidden = true;
  els.fallback.hidden = false;
  const fallback = project.fallback || {};
  els.fallbackReason.textContent = fallback.reason || "This program needs something the browser arcade can't provide.";
  const href = safeHttpUrl(fallback.href || "");
  if (href) {
    els.fallbackLink.hidden = false;
    els.fallbackLink.href = href;
    els.fallbackLink.textContent = fallback.linkLabel || "Open the other site";
  } else {
    els.fallbackLink.hidden = true;
  }
  els.toggleCode.hidden = false;
  showCode(true);
  els.hint.textContent = HINTS.fallback;
}

async function runGame(focusInput) {
  const ticket = ++runId;
  turtlePlayback += 1;
  busy = true;
  setStatus("running");
  els.go.disabled = true;
  els.choiceTrue.disabled = true;
  els.choiceFalse.disabled = true;
  els.restart.disabled = true;
  try {
    const pyodide = await ensurePyodide();
    if (ticket !== runId) return;
    writeFs(pyodide, baseName(project.entry), files[0].text);
    for (const file of files) {
      if (file.path) writeFs(pyodide, file.path, file.text);
    }
    const engine = await loadEngine();
    pyodide.globals.set("USER_SOURCE", files[0].text);
    pyodide.globals.set("USER_ANSWERS_JSON", JSON.stringify(answers));
    pyodide.globals.set("USER_SEED", seed);
    pyodide.globals.set("USER_FILENAME", baseName(project.entry));
    const returned = pyodide.runPython(engine);
    if (returned && typeof returned.destroy === "function") returned.destroy();
    if (ticket !== runId) return;
    const result = JSON.parse(readResult(pyodide));
    paintResult(result, focusInput);
  } catch (error) {
    if (ticket !== runId) return;
    paintResult({
      status: "error",
      output: "",
      prompt: "",
      error: error && error.message ? error.message : String(error),
    }, false);
  } finally {
    if (ticket === runId) {
      busy = false;
      els.go.disabled = false;
      els.choiceTrue.disabled = false;
      els.choiceFalse.disabled = false;
      els.restart.disabled = false;
      document.body.dataset.run = String(runId);
    }
  }
}

function paintResult(result, focusInput) {
  setStatus(result.status || "error");
  const holdResult = shouldHoldTurtleResult(result);
  paintTurtle(result.turtle, holdResult ? function () { revealTurtleResult(result); } : null);
  const earlyOutput = holdResult ? (result.turtle.outputBeforeMotion || "") : (result.output || "");
  els.termOut.textContent = earlyOutput || (result.status === "done" && !holdResult ? "(The program finished without printing anything.)" : "");
  const prompt = tidyPrompt(result.prompt);
  const trueFalse = usesTrueFalseButtons(result.status);
  els.termPrompt.hidden = result.status !== "need_input";
  els.termDone.hidden = result.status !== "done" || holdResult;
  els.composer.hidden = result.status !== "need_input";
  els.choices.hidden = !trueFalse;
  els.composerRow.hidden = trueFalse;
  els.restart.hidden = false;
  els.toggleCode.hidden = false;
  if (result.status === "need_input") {
    els.termPrompt.textContent = prompt;
    els.answerLabel.textContent = prompt;
    els.answer.setAttribute("aria-label", prompt);
    els.choices.setAttribute("aria-label", prompt);
    els.answer.value = "";
    if (focusInput) {
      if (trueFalse) els.choiceTrue.focus();
      else els.answer.focus();
    }
  }
  if (result.error) {
    els.termError.hidden = false;
    els.termError.textContent = result.error;
  } else {
    els.termError.hidden = true;
    els.termError.textContent = "";
  }
  els.undo.hidden = !(result.status === "error" && answers.length);
  if (holdResult) els.hint.textContent = HINTS.running;
  else els.hint.textContent = trueFalse ? HINTS.true_false : (HINTS[result.status] || HINTS.error);
  els.termScroll.scrollTop = els.termScroll.scrollHeight;
}

function shouldHoldTurtleResult(result) {
  const frames = result.turtle && result.turtle.frames;
  if (!frames || frames.length < 2) return false;
  if (result.status !== "done") return false;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return false;
  return true;
}

function revealTurtleResult(result) {
  els.termOut.textContent = result.output || "(The program finished without printing anything.)";
  els.termDone.hidden = result.status !== "done";
  els.hint.textContent = HINTS[result.status] || HINTS.error;
  els.termScroll.scrollTop = els.termScroll.scrollHeight;
}

function paintTurtle(scene, onDone) {
  const token = ++turtlePlayback;
  if (!scene || typeof scene.width !== "number" || typeof scene.height !== "number") {
    els.turtleStage.hidden = true;
    return;
  }
  const canvas = els.turtleCanvas;
  canvas.width = scene.width;
  canvas.height = scene.height;
  canvas.setAttribute("aria-label", "Turtle screen, " + scene.width + " by " + scene.height);
  els.turtleStage.hidden = false;
  const frames = Array.isArray(scene.frames) ? scene.frames : [];
  if (!frames.length) {
    drawTurtleFrame(canvas, scene, null);
    return;
  }
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || frames.length === 1) {
    drawTurtleFrame(canvas, scene, frames[frames.length - 1]);
    if (onDone) onDone();
    return;
  }
  drawTurtleFrame(canvas, scene, frames[0]);
  const duration = Math.min(4200, Math.max(1400, frames.length * 7));
  const start = performance.now();
  let lastIndex = 0;
  function tick(now) {
    if (token !== turtlePlayback) return;
    const progress = Math.min(1, (now - start) / duration);
    const index = Math.min(frames.length - 1, Math.floor(progress * frames.length));
    if (index !== lastIndex) {
      drawTurtleFrame(canvas, scene, frames[index]);
      lastIndex = index;
    }
    if (progress < 1) requestAnimationFrame(tick);
    else if (onDone) onDone();
  }
  requestAnimationFrame(tick);
}

function drawTurtleFrame(canvas, scene, frame) {
  const ctx = canvas.getContext("2d");
  const width = scene.width;
  const height = scene.height;
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = scene.bg || "#ffffff";
  ctx.fillRect(0, 0, width, height);
  const lines = Array.isArray(scene.lines) ? scene.lines : [];
  const count = frame && typeof frame.lineCount === "number" ? frame.lineCount : 0;
  ctx.lineCap = "round";
  ctx.lineJoin = "round";
  for (let i = 0; i < count && i < lines.length; i += 1) {
    const line = lines[i];
    ctx.beginPath();
    ctx.strokeStyle = line.color || "#000000";
    ctx.lineWidth = line.width || 1;
    ctx.moveTo(width / 2 + line.x1, height / 2 - line.y1);
    ctx.lineTo(width / 2 + line.x2, height / 2 - line.y2);
    ctx.stroke();
  }
  const turtles = frame && Array.isArray(frame.turtles) ? frame.turtles : [];
  turtles.forEach((turtle) => {
    if (!turtle || turtle.visible === false) return;
    drawOneTurtle(ctx, width, height, turtle);
  });
}

function drawOneTurtle(ctx, width, height, turtle) {
  const heading = Number(turtle.heading) || 0;
  const radians = heading * Math.PI / 180;
  const e0 = Math.cos(radians);
  const e1 = Math.sin(radians);
  const originX = Number(turtle.x) || 0;
  const originY = Number(turtle.y) || 0;
  ctx.beginPath();
  TURTLE_SHAPE.forEach((point, index) => {
    const x = point[0];
    const y = point[1];
    const worldX = originX + (e1 * x + e0 * y);
    const worldY = originY + (-e0 * x + e1 * y);
    const screenX = width / 2 + worldX;
    const screenY = height / 2 - worldY;
    if (index === 0) ctx.moveTo(screenX, screenY);
    else ctx.lineTo(screenX, screenY);
  });
  ctx.closePath();
  ctx.fillStyle = turtle.fill || turtle.color || "#000000";
  ctx.strokeStyle = "#1a1020";
  ctx.lineWidth = 1.5;
  ctx.fill();
  ctx.stroke();
}

function usesTrueFalseButtons(status) {
  return status === "need_input" && project && project.id === "quiz-game";
}

function onChoice(value) {
  if (busy || document.body.dataset.status !== "need_input") return;
  if (!usesTrueFalseButtons("need_input")) return;
  answers.push(value);
  runGame(true);
}

function onSubmit(event) {
  event.preventDefault();
  if (busy || document.body.dataset.status !== "need_input") return;
  answers.push(els.answer.value);
  runGame(true);
}

function onRestart() {
  if (busy) return;
  answers = [];
  if (!seedLocked) seed = Math.floor(Math.random() * 1000000000) + 1;
  runGame(true);
}

function onUndo() {
  if (busy || !answers.length) return;
  answers.pop();
  runGame(true);
}

function onToggleCode() {
  showCode(els.codePanel.hidden);
}

function showCode(open) {
  els.codePanel.hidden = !open;
  els.toggleCode.setAttribute("aria-expanded", open ? "true" : "false");
  els.toggleCode.textContent = open ? "Hide the code" : "View the code";
  if (!open) return;
  fillPicker();
  showSelectedFile();
}

function fillPicker() {
  const several = files.length > 1;
  els.codePicker.hidden = !several;
  els.codeName.hidden = several;
  els.codePicker.replaceChildren();
  files.forEach((file, index) => {
    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = file.name;
    els.codePicker.appendChild(option);
  });
  if (!several && files[0]) els.codeName.textContent = files[0].name;
}

function showSelectedFile() {
  const index = files.length > 1 ? Number(els.codePicker.value || 0) : 0;
  const file = files[index];
  els.codeText.textContent = file ? file.text : "";
}

async function onCopy() {
  const text = els.codeText.textContent || "";
  try {
    await navigator.clipboard.writeText(text);
    els.copy.textContent = "Copied!";
  } catch (error) {
    els.copy.textContent = "Select the code and copy it";
  }
  setTimeout(() => {
    els.copy.textContent = "Copy the code";
  }, 1600);
}

function readResult(pyodide) {
  const proxy = pyodide.globals.get("ARCADE_RESULT");
  if (typeof proxy === "string") return proxy;
  const raw = proxy.toString();
  if (proxy && typeof proxy.destroy === "function") proxy.destroy();
  return raw;
}

function ensurePyodide() {
  if (!pyodidePromise) {
    if (typeof loadPyodide !== "function") {
      return Promise.reject(new Error("Python couldn't download. Check your internet connection and refresh the page."));
    }
    pyodidePromise = loadPyodide({ indexURL: PYODIDE_BASE });
  }
  return pyodidePromise;
}

function loadEngine() {
  if (!enginePromise) enginePromise = loadText("engine.py");
  return enginePromise;
}

async function loadText(url) {
  const response = await fetch(url, { cache: "no-cache" });
  if (!response.ok) {
    throw new Error("Couldn't find " + url + " (" + response.status + "). Check the path in projects.json.");
  }
  return response.text();
}

function writeFs(pyodide, path, text) {
  const parts = path.split("/");
  let dir = "/home/pyodide";
  for (let i = 0; i < parts.length - 1; i += 1) {
    dir += "/" + parts[i];
    try { pyodide.FS.mkdir(dir); } catch (error) { /* already there */ }
  }
  pyodide.FS.writeFile("/home/pyodide/" + path, text);
}

function setStatus(status) {
  document.body.dataset.status = status;
  if (status === "loading" || status === "running") els.hint.textContent = HINTS[status];
}

function fail(message) {
  setStatus("error");
  els.title.textContent = "Can't open that game";
  els.terminal.hidden = true;
  els.pageError.hidden = false;
  els.pageError.textContent = message;
  els.hint.textContent = "";
}

function tidyPrompt(prompt) {
  const trimmed = String(prompt || "").replace(/\s+$/u, "");
  return trimmed || "The program is waiting for you to type something.";
}

function prettyPath(entry) {
  return String(entry || "").replace(/^\.\.\//, "");
}

function baseName(path) {
  const parts = String(path || "").split("/");
  return parts[parts.length - 1] || "game.py";
}

function safeHttpUrl(value) {
  try {
    const url = new URL(value, window.location.href);
    if (url.protocol === "http:" || url.protocol === "https:") return url.href;
  } catch (error) {
    return "";
  }
  return "";
}

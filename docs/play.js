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
  composer: document.getElementById("composer"),
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

const params = new URLSearchParams(location.search);
const seedParam = params.get("seed");
if (seedParam && /^\d+$/.test(seedParam)) {
  seed = Number(seedParam);
  seedLocked = true;
}

els.composer.addEventListener("submit", onSubmit);
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
  const parts = [];
  if (project.dayLabel) parts.push(project.dayLabel);
  else if (typeof project.day === "number") parts.push("Day " + project.day);
  if (project.badge) parts.push(project.badge);
  els.kicker.textContent = parts.join(" · ");
  els.title.textContent = project.title;
  document.title = project.title + " · Plumber to Programmer Arcade";
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
  busy = true;
  setStatus("running");
  els.go.disabled = true;
  els.restart.disabled = true;
  try {
    const pyodide = await ensurePyodide();
    if (ticket !== runId) return;
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
      els.restart.disabled = false;
      document.body.dataset.run = String(runId);
    }
  }
}

function paintResult(result, focusInput) {
  setStatus(result.status || "error");
  els.termOut.textContent = result.output || (result.status === "done" ? "(The program finished without printing anything.)" : "");
  els.termPrompt.hidden = result.status !== "need_input";
  els.termDone.hidden = result.status !== "done";
  els.composer.hidden = result.status !== "need_input";
  els.restart.hidden = false;
  els.toggleCode.hidden = false;
  if (result.status === "need_input") {
    const prompt = tidyPrompt(result.prompt);
    els.termPrompt.textContent = prompt;
    els.answerLabel.textContent = prompt;
    els.answer.setAttribute("aria-label", prompt);
    els.answer.value = "";
    if (focusInput) els.answer.focus();
  }
  if (result.error) {
    els.termError.hidden = false;
    els.termError.textContent = result.error;
  } else {
    els.termError.hidden = true;
    els.termError.textContent = "";
  }
  els.undo.hidden = !(result.status === "error" && answers.length);
  els.hint.textContent = HINTS[result.status] || HINTS.error;
  els.termScroll.scrollTop = els.termScroll.scrollHeight;
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

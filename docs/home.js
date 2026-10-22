"use strict";

const grid = document.getElementById("grid");
const count = document.getElementById("count");
const pageError = document.getElementById("page-error");

init();

async function init() {
  if (location.protocol === "file:") {
    showError("Open this site through a small local server. Double-clicking the HTML file will not load the games. The steps are in ADDING_A_GAME.md.");
    return;
  }
  try {
    const response = await fetch("projects.json", { cache: "no-cache" });
    if (!response.ok) {
      throw new Error("Could not load projects.json (" + response.status + ").");
    }
    const data = JSON.parse(await response.text());
    if (!data || !Array.isArray(data.projects)) {
      throw new Error("projects.json needs a projects list.");
    }
    render(data.projects);
  } catch (error) {
    const message = error instanceof SyntaxError
      ? "projects.json isn't valid JSON. Check commas and quotes. " + error.message
      : error.message;
    showError(message);
  }
}

function render(projects) {
  grid.replaceChildren();
  const games = projects.filter((project) => project && project.id && project.title);
  count.textContent = games.length === 1 ? "1 game" : games.length + " games";
  if (!games.length) {
    showError("No games yet. Add one to projects.json. The steps are in ADDING_A_GAME.md.");
    return;
  }
  games.forEach((project, index) => {
    grid.appendChild(cardFor(project, index));
  });
}

function cardFor(project, index) {
  const link = document.createElement("a");
  link.className = "card";
  link.href = "play.html?id=" + encodeURIComponent(project.id);
  link.style.backgroundColor = safeColor(project.accent, index);
  link.dataset.projectId = project.id;

  const top = document.createElement("div");
  top.className = "card-top";
  top.appendChild(el("p", "daychip", dayText(project)));
  if (project.badge) top.appendChild(el("p", "badge", project.badge));
  link.appendChild(top);

  link.appendChild(el("h2", null, project.title));
  link.appendChild(el("p", "desc", project.description || ""));
  link.appendChild(el("p", "play-label", isPlayable(project) ? "Play →" : "How to run it →"));

  const mark = el("p", "watermark", dayNum(project));
  mark.setAttribute("aria-hidden", "true");
  link.appendChild(mark);
  return link;
}

function isPlayable(project) {
  return project.playable !== false;
}

function dayText(project) {
  if (project.dayLabel) return project.dayLabel;
  if (typeof project.day === "number") return "Day " + project.day;
  return "Game";
}

function dayNum(project) {
  if (typeof project.day === "number") return String(project.day).padStart(2, "0");
  return "★";
}

function safeColor(value, index) {
  const fallback = ["#ffe14a", "#7ee0c6", "#ffb3c7", "#9dc7ff", "#ffbf80", "#d4c2ff"];
  return /^#[0-9a-fA-F]{6}$/.test(value || "") ? value : fallback[index % fallback.length];
}

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text != null) node.textContent = text;
  return node;
}

function showError(message) {
  count.textContent = "Games couldn't load";
  pageError.hidden = false;
  pageError.textContent = message;
}

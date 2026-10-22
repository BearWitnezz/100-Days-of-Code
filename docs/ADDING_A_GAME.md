# Add a game to the arcade

The homepage is a list of cards. That list lives in `projects.json` in this same folder. Each block in the list is one card. The Python file stays where you already saved it. You do not copy it into `docs`.

## 1. Save your program

Put the `.py` file in one of these places:

- A practice project you wrote yourself: `day-10/practice/my_game.py`
- A bigger milestone: `milestones/my_game.py`

Use normal Python. `print()` shows up in the terminal on the play page. `input()` stops and waits for the text box.

Leave the lesson copies in the main `day-XX` folders off the list. The arcade is for your versions.

## 2. Add a block to projects.json

Open `docs/projects.json`. Copy the last game, from its `{` through its `}`. Paste a new block after it. Put a comma after the `}` of the game before yours. Do not put a comma after the very last `}`.

Change these fields:

- `id` is the short name in the link. Use lowercase letters, numbers, and dashes, like `my-game`. Every game needs its own id.
- `title` is the big name on the card.
- `day` is the day number, like `10`. For a milestone you can use `"dayLabel": "Days 1–8"` instead.
- `description` is the one sentence on the card.
- `howToPlay` is one sentence on the play page that says what to type.
- `entry` is the path from this `docs` folder to your file. A file at `day-10/practice/my_game.py` uses `"entry": "../day-10/practice/my_game.py"`.
- `accent` is the card color, like `"#ffe14a"`. Pick a color the other cards are not already using.
- `badge` is optional. `"Milestone"` or `"Rebuild"` shows a small label on the card.

Here is a whole block you can copy:

```json
{
  "id": "my-game",
  "title": "My Game",
  "day": 10,
  "description": "One sentence about what the player does.",
  "howToPlay": "Say what they should type.",
  "entry": "../day-10/practice/my_game.py",
  "accent": "#9dc7ff"
}
```

Save the file.

## 3. Play it on your computer

Open a terminal in the main project folder. That is the folder that contains `day-01` and `docs`. Run:

```bash
python -m http.server 8000
```

In the browser, open:

http://localhost:8000/docs/

Click your new card. The page runs the same `.py` file you saved.

Do not open the HTML file by double-clicking it. The browser will not be allowed to read the Python files that way.

The first game takes a few seconds. The page is downloading Python into the browser. That is normal.

## If your program imports another file you wrote

Some programs split the word list or the logo into a second file. Add a `files` list. `path` is the file name your `import` expects. `src` is where that file lives in the repo.

If `main.py` says `from words import word_list`, then `path` is `words.py`.

```json
"entry": "../day-10/practice/main.py",
"files": [
  { "path": "words.py", "src": "../day-10/practice/words.py" }
]
```

## If the browser cannot run it

Reeborg's maze is the example. It calls `move()` and `turn_left()`. Those commands exist on Reeborg's website, not in normal Python, so the arcade cannot play that one.

Set `"playable": false` and add a `fallback` block. The card will say "How to run it". The page shows your code, a copy button, and a link.

```json
{
  "id": "reeborg-maze",
  "title": "Lost in a Maze",
  "day": 6,
  "description": "Walk Reeborg the robot out of a maze.",
  "howToPlay": "Copy the code into Reeborg's maze.",
  "entry": "../day-06/reeborg_maze.py",
  "accent": "#b6f2a8",
  "playable": false,
  "fallback": {
    "reason": "This program uses robot commands that only exist on Reeborg's website.",
    "href": "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json",
    "linkLabel": "Open the maze on Reeborg's site"
  }
}
```

Copy the code, open the link, and paste it into Reeborg.

## Put the arcade on the internet

GitHub Pages can host this site for free. The Python files have to be on the same site as the pages, so publish the whole repo, not only the `docs` folder.

1. On GitHub, open this repo.
2. Click **Settings**.
3. Click **Pages** in the left sidebar.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Set the branch to **main** and the folder to **/ (root)**.
6. Click **Save**.
7. Wait a minute and refresh that settings page. GitHub shows a site address like `https://bearwitnezz.github.io/100-Days-of-Code/`.
8. The arcade is that address plus `docs/`:

https://bearwitnezz.github.io/100-Days-of-Code/docs/

Leave the folder on **/ (root)**. Do not switch it to `/docs`. The `/docs` choice uploads only this folder and leaves the `.py` files behind, so the games cannot start.

The flashcards stay at:

https://bearwitnezz.github.io/100-Days-of-Code/flashcards/

If that flashcards link already works, Pages is already on. After this arcade is on the `main` branch, open the `docs/` address above. You do not create a second site.

## Colors you can use

`#ffe14a` yellow, `#7ee0c6` mint, `#ffb3c7` pink, `#9dc7ff` blue, `#ffbf80` orange, `#d4c2ff` purple, `#b6f2a8` green, `#ffd0a8` peach, `#c6d4ff` periwinkle, `#ffc2ef` magenta, `#b8f0ee` teal, `#f8d49a` sand.

## If the homepage says projects.json has a problem

JSON is picky. A missing comma, an extra comma, or a forgotten quote will blank the game list. The message on the page points at the spot. Fix it, save, and refresh.

To take a game off the arcade, delete its block in `projects.json`. Leave the `.py` file where it is.

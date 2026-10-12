# Day 7: Hangman

Run `main.py`. It pulls the word list from `hangman_words.py` and the ASCII art from `hangman_art.py`.

## Bugs I fixed along the way

- My for loop originally reused the name `guess`, which overwrote the letter the player typed.
- `display` kept growing on every guess instead of resetting, so I reset it at the start of each turn.
- The lose check was in an `elif` chain where it couldn't run on the same turn that took the last life. I split it into separate `if` checks and added `and lives > 0` to the while condition.
- I added a `guessed_letters` list, so guessing the same wrong letter again shows a message instead of costing another life.

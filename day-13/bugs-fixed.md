# Day 13 – Bugs I Fixed (Hangman rebuild)

1. **Can't change a string.** The blanks were a string, so `word[position] = guess` didn't work. Fix: keep the blanks in a list.
2. **Getting the positions.** Used `range(len(random_word))` to loop over the indexes so a correct guess could go in the right spot.
3. **Showing dashes, not a list.** Rebuilt `display` as a string by looping and adding each letter with `+=` instead of printing the list.
4. **Repeat guess "won" the game.** `display = ""` was reset at the top of the loop, so a repeat guess left it empty. Fix: reset it right before rebuilding it.
5. **Still printing after 0 lives.** Moved the lives check right after `lives -= 1`, and put "Incorrect guess" under an `else`.
6. **Showing the drawing.** Printed `stages[lives]`. The game ends at 0 lives, when the full figure shows.

Day 7 proof project — Guess the Fitting. Plumbing hangman that uses random.choice, a display list, a while loop with a game_over flag, and a for position in range(len(word)) loop to reveal letters. Lives are lost on wrong guesses.

## Rebuild
`guess_the_fitting_rebuild.py` is John’s next-day from-memory rebuild. It keeps guessed letters in a `guessed_words` list, so a repeat guess shows a message instead of costing a life.

## Second rebuild
`guess_the_fitting_rebuild2.py` is John’s second rebuild, written from memory with no help. It still includes the repeated-guess bonus: a letter already guessed shows a message instead of costing a life.

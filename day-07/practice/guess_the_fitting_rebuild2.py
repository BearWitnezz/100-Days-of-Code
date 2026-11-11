# TODO 1: Import random. The fittings are valve, anglestop, elbow, and wastearm.

# TODO 2: Start the board as an empty list, lives at 6, game_over as False, and an empty already-guessed list.

# TODO 3: Pick one fitting at random. Print "Welcome to Guess the Fitting!".

# TODO 4: Append one "_" for each letter, and print the board.

# TODO 5: Loop while the game is not over. Ask "Guess a letter: " and lowercase it.

# TODO 6: If the letter is not in the fitting and has not been guessed, lose one life, print the lives that are
#   left and the board, and record the guess.

# TODO 7: If that miss was already guessed, print "You already guessed {letter}!" and the board. Do not take
#   another life.

# TODO 8: If the letter is in the fitting but was already guessed, print that same already-guessed message and
#   the board.

# TODO 9: Otherwise, fill the letter into every matching position, record it, and print the board.

# TODO 10: Stop when lives hit 0 or the board has no "_" left.

# TODO 11: On a loss, print "You lost! The word was " and the fitting. On a cleared board, print "You win!".

import random
plumbing_words = ["valve", "anglestop", "elbow", "wastearm"]
word = []
lives = 6
game_over = False
computer_choice = random.choice(plumbing_words)
already_guessed = []
print("Welcome to Guess the Fitting!")
for letter in computer_choice:
    word.append("_")
print(word)
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess not in computer_choice:
        if guess not in already_guessed:
            lives -= 1
            print(f"Wrong guess! You have {lives} lives left!")
            print(word)
            already_guessed.append(guess)
        else:
            print(f"You already guessed {guess}!")
            print(word)
    elif guess in already_guessed:
        print(f"You already guessed {guess}!")
        print(word)
    else:
        for position in range(len(computer_choice)):
            if guess == computer_choice[position]:
                word[position] = guess
                already_guessed.append(guess)
        print(word)
    if lives == 0 or "_" not in word:
        game_over = True
        if lives == 0:
            print(f"You lost! The word was {computer_choice}")
        elif "_" not in word:
            print(f"You win!")

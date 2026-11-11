# TODO 1: Import random. The fittings are valve, anglestop, elbow, and wastearm.

# TODO 2: Start the board as an empty list, lives at 6, game_over as False, and an empty list of guessed letters.

# TODO 3: Pick one fitting at random. Print "Welcome to Guess the Fitting!".

# TODO 4: Add one "_" to the board for each letter in the fitting, and print the board.

# TODO 5: Loop while the game is not over. Ask "Guess a letter: " and lowercase it.

# TODO 6: A new miss (not in the fitting, and not already guessed) loses one life, prints how many lives are left
#   and the board, and records the letter.

# TODO 7: A letter that was already guessed prints "You already guessed this letter." and the board. It does not
#   cost a life.

# TODO 8: A new hit walks the fitting by position, fills that letter in everywhere it belongs, records the guess,
#   and prints the board.

# TODO 9: When the board has no "_" left, the game is over and you print "You win!".

# TODO 10: At 0 lives, the game is over. Print "You lose! The word was " and the fitting.

import random
plumbing_words = ["valve", "anglestop", "elbow", "wastearm"]
word = []
lives = 6
game_over = False
computer_choice = random.choice(plumbing_words)
guessed_words = []
print("Welcome to Guess the Fitting!")
for letter in range(len(computer_choice)):
    word += "_"
print(word)
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess not in computer_choice and guess not in guessed_words:
        lives -= 1
        print(f"Incorrect guess. You have {lives} left.")
        print(word)
        guessed_words.append(guess)
    elif guess in guessed_words:
        print("You already guessed this letter.")
        print(word)
    else:
        for position in range(len(computer_choice)):
            if computer_choice[position] == guess:
                word[position] = guess
        guessed_words.append(guess)
        print(word)
    if "_" not in word:
        game_over = True
        print("You win!")
    if lives == 0:
        game_over = True
        print(f"You lose! The word was {computer_choice}")

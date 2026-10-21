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

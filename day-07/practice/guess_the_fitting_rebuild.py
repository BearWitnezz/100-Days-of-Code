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

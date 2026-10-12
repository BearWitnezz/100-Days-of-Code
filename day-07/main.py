from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

import random
lives = 6

print(logo)
chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

correct_letters = []
guessed_letters = []
display = ""

while display != chosen_word and lives > 0:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in guessed_letters:
        print("You already guessed this letter!")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You win!")
    if guess not in chosen_word and guess not in guessed_letters:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        if lives == 0:
            print(f"It was {chosen_word}! You lose!")
    print(stages[lives])
    guessed_letters.append(guess)

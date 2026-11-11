# TODO 1: Import the word list, the logo, and the hangman stages. Import random. Start with 6 lives.

# TODO 2: Print the logo, then pick one word at random from the word list.

# TODO 3: Build a placeholder of one "_" for every letter in that word, and print it.

# TODO 4: Keep two lists: letters that have been found, and letters the player has already guessed. Start the
#   display as an empty string.

# TODO 5: Loop while the display is not the chosen word and lives are still above 0. Ask "Guess a letter: " and
#   lowercase it. Reset the display to an empty string at the start of every guess.
#   Nudge: don't reuse the name guess inside the letter loop, or you overwrite the letter the player typed.

# TODO 6: If that letter is already in the guessed list, print "You already guessed this letter!".

# TODO 7: Rebuild the display from the chosen word. Where the guess matches, show that letter and record it in the
#   found-letters list. Where a letter is already in the found list, show it. Everywhere else, use "_". Print the
#   display.

# TODO 8: If the display has no "_" left, print "You win!".

# TODO 9: A miss that has not been guessed before prints that the letter is not in the word, subtracts 1 life, and
#   prints how many lives are left out of 6. At 0 lives, print the word and "You lose!".
#   Nudge: a repeat of a wrong letter must not take another life.

# TODO 10: Print the hangman stage for the lives that are left, then add this guess to the guessed-letters list.

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

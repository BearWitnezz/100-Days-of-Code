# TODO 1: Import random and the logo from art.

# TODO 2: Define make_a_guess(attempts) with a docstring. Print how many attempts are left, then loop until the
#   game is over.

# TODO 3: Ask "Make a guess: ". If the answer is all digits, turn it into an int.

# TODO 4: A guess equal to the secret number ends the game and prints "You got it! The answer was {number}."

# TODO 5: A guess below the secret prints "Too low." and costs one attempt. A guess above it prints "Too high."
#   and costs one attempt. While attempts remain, print "Guess again." and how many attempts are left.

# TODO 6: A guess that is not a whole number also costs one attempt. While attempts remain, print "Guess again."
#   and the attempts that are left.

# TODO 7: At 0 attempts, end the game and print "You've run out of guesses. The number was {number}. Refresh the
#   page to run again."

# TODO 8: Print the logo. Then print "Welcome to the Number Guessing Game!" and "I'm thinking of a number between
#   1 and 100."

# TODO 9: Pick the secret number with random.randint from 1 to 100.

# TODO 10: Ask "Choose a difficulty. Type 'easy' or 'hard': " and lowercase the answer. "easy" calls make_a_guess
#   with 10 attempts. Any other answer calls it with 5.

import random
from art import logo
def make_a_guess(attempts):
        """Take guesses until the number is found or the attempts run out."""
        game_over = False
        print(f"You have {attempts} attempts remaining to guess the number.")
        while not game_over:
            guess = input("Make a guess: ")
            if guess.isdigit():
                guess = int(guess)
                if guess == secret_number:
                    game_over = True
                    print(f"You got it! The answer was {secret_number}.")
                else:
                    if guess < secret_number:
                        print("Too low.")
                        attempts -= 1
                        if attempts > 0:
                            print("Guess again.")
                            remaining_attempts = f"You have {attempts} attempts remaining to guess the number."
                            print(remaining_attempts)
                    elif guess > secret_number:
                        print("Too high.")
                        attempts -= 1
                        if attempts > 0:
                            print("Guess again.")
                            remaining_attempts = f"You have {attempts} attempts remaining to guess the number."
                            print(remaining_attempts)
            else:
                attempts -= 1
                if attempts > 0:
                    print("Guess again.")
                    remaining_attempts = f"You have {attempts} attempts remaining to guess the number."
                    print(remaining_attempts)
            if attempts == 0:
                game_over = True
                print(f"You've run out of guesses. The number was {secret_number}. Refresh the page to run again.")

print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
secret_number = random.randint(1,100)
# print(secret_number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    make_a_guess(attempts = 10)
else:
    make_a_guess(attempts = 5)

import random
from art import logo
def make_a_guess(attempts):
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

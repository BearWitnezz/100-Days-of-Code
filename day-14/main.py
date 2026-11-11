# TODO 1: Show the logo and pick two different accounts to compare.
# TODO 2: Print each account as its name, description, and country, with the vs art between them.
# TODO 3: Ask who has more followers, A or B, and check that guess.
# TODO 4: On a correct guess, add a point, move B into A's place, and draw a new B.
# TODO 5: On a wrong guess, end the game and print the final score.

print("Welcome to Higher or Lower!")
import random
from art import logo
from art import vs
from game_data import data
def format_account(account):
    """Return an account as its name, description, and country."""
    return f"{account["name"]}, {account["description"]}, {account["country"]}"
def check_answer(guess, a_followers, b_followers):
    """Return True when the guess names the account with more followers."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
game_over = False
print(logo)
score = 0
account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)
compare_a = format_account(account_a)
compare_b = format_account(account_b)
print(f"Compare A: {compare_a}")
print(vs)
print(f"Against B: {compare_b}")
while not game_over:
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(user_choice, account_a["follower_count"], account_b["follower_count"])
    if is_correct:
        score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score: {score}")
        compare_a = compare_b
        account_a = account_b
        print(f"Compare A: {compare_a}")
        print(vs)
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
        compare_b = format_account(account_b)
        print(f"Against B: {compare_b}")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")

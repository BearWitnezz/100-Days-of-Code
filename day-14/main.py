# TODO 1: Print "Welcome to Higher or Lower!". Import random, the logo, the vs art, and the account data.

# TODO 2: Define format_account(account) with a docstring. It returns the account's name, description, and
#   country in one string, separated by commas.

# TODO 3: Define check_answer(guess, a_followers, b_followers) with a docstring. Return True when the guess is
#   "a" and A has more followers, or when the guess is "b" and B has at least as many.

# TODO 4: Start the game as not over. Print the logo. Start the score at 0.

# TODO 5: Pick two accounts at random for A and B. If they are the same account, pick B again until they differ.

# TODO 6: Print "Compare A: " plus the formatted A account, then the vs art, then "Against B: " plus the
#   formatted B account.

# TODO 7: Loop while the game is not over. Ask "Who has more followers? Type 'A' or 'B': " and lowercase the
#   answer. Check it against the two follower_count values.

# TODO 8: A correct guess adds 1 to the score, prints 20 blank lines, prints the logo again, and prints
#   "You're right! Current score: " plus the score.

# TODO 9: On that correct guess, move B into A's place. Print Compare A and the vs art, draw a new B that is not
#   the same account as A, format it, and print Against B.

# TODO 10: A wrong guess ends the game and prints "Sorry, that's wrong. Final score: " plus the score.

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

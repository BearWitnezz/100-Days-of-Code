print("Welcome to Higher or Lower!")
import random
from art import logo
from art import vs
from game_data import data
game_over = False
print(logo)
score = 0
account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)
# print(account_a)
# print(account_b)
compare_a = f"{account_a["name"]}, {account_a["description"]}, {account_a["country"]}"
compare_b = f"{account_b["name"]}, {account_b["description"]}, {account_b["country"]}"
print(f"Compare A: {compare_a}")
print(vs)
print(f"Against B: {compare_b}")
while not game_over:
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == "a":
        if account_a["follower_count"] > account_b["follower_count"]:
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
            compare_b = f"{account_b["name"]}, {account_b["description"]}, {account_b["country"]}"
            print(f"Against B: {compare_b}")
        else:
            if account_a["follower_count"] < account_b["follower_count"]:
                game_over = True
                print(f"Sorry, that's wrong. Final score: {score}")
    if user_choice == "b":
        if account_b["follower_count"] > account_a["follower_count"]:
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
            compare_b = f"{account_b["name"]}, {account_b["description"]}, {account_b["country"]}"
            print(f"Against B: {compare_b}")
        else:
            if account_a["follower_count"] > account_b["follower_count"]:
                game_over = True
                print(f"Sorry, that's wrong. Final score: {score}")

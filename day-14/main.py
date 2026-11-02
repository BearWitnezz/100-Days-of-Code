print("Welcome to Higher or Lower!")
import random
from art import logo
from art import vs
from game_data import data
def format_account(account):
    return f"{account["name"]}, {account["description"]}, {account["country"]}"
def check_answer(guess, a_followers, b_followers):
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

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1: Ask the user "What would you like? (espresso/latte/cappuccino):" and save the answer (done)
# TODO 2: Keep asking after each drink, and stop the machine when they type "off" (done)
# TODO 3: When they type "report", print the water, milk, coffee and money left (done)
# TODO 4: Check if there are enough resources for the drink; if not, say "Sorry, there is not enough ___." (done)
# TODO 5: Ask how many quarters, dimes, nickels and pennies, and add up the total (done)
# TODO 6: Check the payment: too little means refund it, enough means add the cost to the money and give change (done)
# TODO 7: Make the coffee: subtract the ingredients and say "Here is your ___ ☕ Enjoy!" (done)

def process_coins():
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies? "))
    total = quarters + dimes + nickles + pennies
    return total
def is_resource_sufficient(order_ingredients):
    enough_resources = True
    for items in order_ingredients:
        # resources["water"] = 20
        # resources["coffee"] = 10
        if resources[items] < order_ingredients[items]:
            print(f"Sorry, there is not enough {items}")
            enough_resources = False
    return enough_resources
money = 0
coffee_machine_off = False
while not coffee_machine_off:
    print("Welcome to the Coffee Machine!")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        coffee_machine_off = True
    elif user_choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Money: ${money}")
    else:
        if is_resource_sufficient(MENU[user_choice]["ingredients"]):
            total = process_coins()
            # print(total)
            if total < MENU[user_choice]["cost"]:
                print("Sorry, there is not enough money")
            else:
                money += MENU[user_choice]["cost"]
                # print(money)
                change = round(total - MENU[user_choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                for items in MENU[user_choice]["ingredients"]:
                    resources[items] -= MENU[user_choice]["ingredients"][items]
                    print(resources[items])
                print(f"Here is your {user_choice} ☕. Enjoy!")


MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


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
            if total < MENU[user_choice]["cost"]:
                print("Sorry, there is not enough money")
            else:
                money += MENU[user_choice]["cost"]
                change = round(total - MENU[user_choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                for items in MENU[user_choice]["ingredients"]:
                    resources[items] -= MENU[user_choice]["ingredients"][items]
                print(f"Here is your {user_choice} ☕. Enjoy!")

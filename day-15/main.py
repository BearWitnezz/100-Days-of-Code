# TODO 1: Store the menu. Espresso needs 50 water and 18 coffee and costs 1.5. Latte needs 200 water, 150 milk,
#   and 24 coffee and costs 2.5. Cappuccino needs 250 water, 100 milk, and 24 coffee and costs 3.0.
#   Each drink has an "ingredients" dictionary and a "cost".

# TODO 2: Start the machine with 300 water, 200 milk, and 100 coffee.

# TODO 3: Define process_coins() with a docstring. Print "Please insert coins." Ask how many quarters, dimes,
#   nickles, and pennies. Return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01.

# TODO 4: Define is_resource_sufficient(order_ingredients) with a docstring. Start a flag at True. For each
#   ingredient, if the machine has less than the order needs, print "Sorry, there is not enough {item}" and set
#   the flag to False. Return the flag.
#   Nudge: set the flag to False inside the shortage check. Don't set it back to True inside the loop.

# TODO 5: Start the money taken at 0, and start the machine as on. Loop until it is turned off.

# TODO 6: Each turn, print "Welcome to the Coffee Machine!" and ask "What would you like?
#   (espresso/latte/cappuccino): ". Lowercase the answer.

# TODO 7: "off" turns the machine off. "report" prints each resource and its amount, then "Money: $" plus the
#   money taken so far.

# TODO 8: For a drink, check that its ingredients are still in stock. Only then ask for the coins.

# TODO 9: If the coins are less than the drink's cost, print "Sorry, there is not enough money".

# TODO 10: Otherwise add the drink's cost to the money, round the change to 2 decimal places, and print
#   "Here is ${change} in change."

# TODO 11: Subtract each ingredient that drink used from the resources, then print "Here is your {drink} ☕.
#   Enjoy!".

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
    """Ask for coins and return the total in dollars."""
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies? "))
    total = quarters + dimes + nickles + pennies
    return total


def is_resource_sufficient(order_ingredients):
    """Return True when every ingredient in the order is still in stock."""
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

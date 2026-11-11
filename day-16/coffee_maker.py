# TODO 1: Define a CoffeeMaker class. It is the machine that holds the ingredients and makes the drink.

# TODO 2: In __init__, give the machine a resources dictionary: 300 water, 200 milk, and 100 coffee.
#   Nudge: anything the object owns needs self. in front of it.

# TODO 3: report() prints three lines from those resources: "Water: {amount}ml", "Milk: {amount}ml", and
#   "Coffee: {amount}g".

# TODO 4: is_resource_sufficient(drink) starts can_make at True. For each item in drink.ingredients, if the
#   drink needs more than the machine has, print "Sorry there is not enough {item}." and set can_make to False.
#   Return can_make.

# TODO 5: make_coffee(order) subtracts each of order.ingredients from the resources, then prints
#   "Here is your {order.name} ☕️. Enjoy!".

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        """Set the starting amounts of water, milk, and coffee."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

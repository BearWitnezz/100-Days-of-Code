# TODO 1: Define a MenuItem class. __init__ takes a name, water, milk, coffee, and cost.

# TODO 2: Save the name and the cost on the item. Store water, milk, and coffee together in an ingredients
#   dictionary.

# TODO 3: Define a Menu class. In __init__, build a list of three MenuItem drinks:
#   latte (200 water, 150 milk, 24 coffee, cost 2.5),
#   espresso (50 water, 0 milk, 18 coffee, cost 1.5),
#   cappuccino (250 water, 50 milk, 24 coffee, cost 3).

# TODO 4: get_items() walks that list and returns every drink name with a "/" after it, as one string.

# TODO 5: find_drink(order_name) walks the menu. When a drink's name matches, return that MenuItem.

# TODO 6: If no drink matches, print "Sorry that item is not available."

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        """Store one drink's name, cost, and ingredient amounts."""
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        """Create the list of drinks the machine can make."""
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

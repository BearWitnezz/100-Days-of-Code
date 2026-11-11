# TODO 1: Define a MoneyMachine class. It takes payment and tracks profit.

# TODO 2: Give the class a CURRENCY of "$" and a COIN_VALUES dictionary: quarters 0.25, dimes 0.10, nickles 0.05,
#   and pennies 0.01.

# TODO 3: In __init__, start profit at 0 and money_received at 0.

# TODO 4: report() prints "Money: " plus the currency symbol and the profit.

# TODO 5: process_coins() prints "Please insert coins." For each coin in COIN_VALUES, ask "How many {coin}?: ",
#   multiply that count by the coin's value, and add it to money_received. Return money_received.

# TODO 6: make_payment(cost) calls process_coins(). If money_received covers the cost, round the change to 2
#   decimal places, print "Here is {currency}{change} in change.", add the cost to profit, set money_received
#   back to 0, and return True.

# TODO 7: If the money is short, print "Sorry that's not enough money. Money refunded.", set money_received
#   back to 0, and return False.

class MoneyMachine:
    """Models the machine that takes payment and tracks profit."""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        """Start with no profit and no coins received."""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

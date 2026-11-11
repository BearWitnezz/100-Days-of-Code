# TODO 1: Import Menu, CoffeeMaker, and MoneyMachine.

# TODO 2: Create one menu, one coffee maker, and one money machine.

# TODO 3: Ask the menu for its drink list once, before the loop, so the prompt can show every drink.

# TODO 4: Loop until the machine is off. Ask "What would you like? {drinks}: " and lowercase the answer.

# TODO 5: "off" stops the loop.

# TODO 6: "report" calls the coffee maker's report and the money machine's report.

# TODO 7: Any other answer is a drink name. Find that drink on the menu.

# TODO 8: If the coffee maker has enough ingredients for that drink, take payment for the drink's cost.
#   Nudge: make_payment takes the price, not the whole drink.

# TODO 9: When that payment goes through, tell the coffee maker to make the drink.
#   Nudge: make_coffee returns nothing, so just call it.

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
get_items = menu.get_items()
coffee_machine_off = False
while not coffee_machine_off:
    user_choice = input(f"What would you like? {get_items}: ").lower()
    if user_choice == "off":
        coffee_machine_off = True
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=user_choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)

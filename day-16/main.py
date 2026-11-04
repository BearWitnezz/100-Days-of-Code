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

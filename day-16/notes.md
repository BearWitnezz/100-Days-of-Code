# Day 16 — OOP intro + OOP Coffee Machine (project day)

Concepts used:

- A class is a blueprint; an object is one instance of it. Attributes are what it has, methods are what it does.
- Class names are PascalCase (`CoffeeMaker`); variables are snake_case (`coffee_maker`). `CoffeeMaker()` with parentheses builds the object.
- `object.attribute` (e.g. `drink.cost`) vs `object.method()` (e.g. `coffee_maker.report()`).
- Treat the provided classes like an external library: read the docs and call their methods, don't edit them.
- `menu.find_drink(order_name=user_choice)` goes inside the loop, after `input()`, with what the user typed.
- `money_machine.make_payment(drink.cost)` takes the price, not the whole drink.
- `coffee_maker.make_coffee(drink)` returns nothing, so just call it (don't save it in a variable).

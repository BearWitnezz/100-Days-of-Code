# Day 15 — Local dev setup + Coffee Machine (project day)

Built from the Coffee Machine roadmap (see /workspace/day15push/Coffee-Machine-Roadmap.pdf). Concepts used:

- Local setup: Python installed on the PC, PyCharm as the editor (projects, run button, the console at the bottom).
- `MENU` is a nested dictionary: `MENU["latte"]["ingredients"]["milk"]` goes drink -> "ingredients" -> item -> amount. `MENU[drink]["cost"]` is the price.
- `resources` holds what the machine has left ("water", "milk", "coffee").
- `is_on = True` and `while is_on:`; typing "off" sets `is_on = False` and the loop ends.
- "report": `for key in resources: print(key, resources[key])` prints each key and its value.
- Coin math: `quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01`.
- `round(x, 2)` rounds change to 2 decimal places (money).
- Flag pattern: `is_enough = True` BEFORE the loop, flipped to `False` only inside the `if` that finds a shortage. Never set back to True inside the loop.
- `process_coins()` returns the total; save it once: `payment = process_coins()`. A bare call throws the result away.
- `is_resource_sufficient(order_ingredients)` loops over its parameter, returns False inside the if, and returns True after the loop.
- Code that should run once per order (asking for coins) goes AFTER the `for item in ...` loop, not inside it.

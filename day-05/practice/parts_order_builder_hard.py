# TODO 1: Import random. Use the same letters (P, V, C, T, E), numbers (0 through 9), and symbols
#   (! @ # $ % ^ & *).

# TODO 2: Start the order code as an empty list, not a string.

# TODO 3: Print "Welcome to the Parts Order Builder".

# TODO 4: Ask how many letters, how many numbers, and how many symbols. Save each answer as an int.

# TODO 5: Append that many random letters, then that many random numbers, then that many random symbols.

# TODO 6: Shuffle the list.

# TODO 7: Walk the shuffled list and join the characters into one new string.

# TODO 8: Print "Your order code is: " and that string.

import random
letters = ["P","V","C","T","E"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*"]
order_code = []
print("Welcome to the Parts Order Builder")
amount_of_letters = int(input("How many letters would you like?\n"))
amount_of_numbers = int(input("How many numbers would you like?\n"))
amount_of_symbols = int(input("How many symbols would you like?\n"))
for picks in range(amount_of_letters):
    order_code.append(random.choice(letters))
for picks in range(amount_of_numbers):
    order_code.append(random.choice(numbers))
for picks in range(amount_of_symbols):
    order_code.append(random.choice(symbols))
random.shuffle(order_code)
new_order_code = ""
for char in order_code:
    new_order_code += char
print(f"Your order code is: {new_order_code}")

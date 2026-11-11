# TODO 1: Import random. Letters are P, V, C, T, and E. Numbers are 0 through 9. Symbols are ! @ # $ % ^ & *.

# TODO 2: Start the order code as an empty string.

# TODO 3: Print "Welcome to the Parts Order Builder".

# TODO 4: Ask how many letters, how many numbers, and how many symbols. Save each answer as an int.

# TODO 5: Add that many random letters onto the code, one character at a time.

# TODO 6: Then add that many random numbers, then that many random symbols, the same way.

# TODO 7: Print "Your order code is: " and the finished code.

import random
letters = ["P","V","C","T","E"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*"]
order_code = ""
print("Welcome to the Parts Order Builder")
amount_of_letters = int(input("How many letters would you like?\n"))
amount_of_numbers = int(input("How many numbers would you like?\n"))
amount_of_symbols = int(input("How many symbols would you like?\n"))
for picks in range(amount_of_letters):
    order_code += random.choice(letters)
for picks in range(amount_of_numbers):
    order_code += random.choice(numbers)
for picks in range(amount_of_symbols):
    order_code += random.choice(symbols)
print(f"Your order code is: {order_code}")

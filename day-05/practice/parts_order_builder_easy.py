# TODO 1: Welcome the user and ask how many letters, numbers, and symbols to use.
# TODO 2: Build the order code in that order by adding one random character at a time.
# TODO 3: Print the finished order code.

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

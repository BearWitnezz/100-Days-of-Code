# TODO 1: Import random. Keep a list of lowercase and uppercase letters, a list of digits 0 through 9, and a list
#   of the symbols ! # $ % & ( ) * +.

# TODO 2: Print "Welcome to the PyPassword Generator!".

# TODO 3: Ask how many letters, how many symbols, and how many numbers. Save each answer as an int.

# TODO 4: Easy version: start the password as an empty string. Add that many random letters, then that many random
#   symbols, then that many random numbers.

# TODO 5: Print the easy password.

# TODO 6: Hard version: collect the same picks in a list instead of a string. Letters first, then symbols, then
#   numbers.

# TODO 7: Shuffle that list, then walk it and join the characters into one string.

# TODO 8: Print the shuffled password.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


#Easy Version
password = ""
for _ in range(nr_letters):
    password += random.choice(letters)
for _ in range(nr_symbols):
    password += random.choice(symbols)
for _ in range(nr_numbers):
    password += random.choice(numbers)
print(password)

#Hard Version
password = []
for _ in range(nr_letters):
    password.append(random.choice(letters))
for _ in range(nr_symbols):
    password.append(random.choice(symbols))
for _ in range(nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
final = ""
for char in password:
    final += char
print(final)

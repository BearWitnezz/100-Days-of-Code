# TODO 1: Import the logo from art.

# TODO 2: Define add, subtract, multiply, and divide. Each takes two numbers, has a docstring, and returns the
#   result. Divide returns the first number divided by the second.

# TODO 3: Map "+", "-", "*", and "/" to those four functions in one dictionary.

# TODO 4: Loop a fresh calculation. Print the logo, ask "What's the first number: " as a float, then print every
#   operation symbol on its own line.

# TODO 5: Ask "Pick an operation: " and "What's the second number: ". Look the symbol up in the dictionary, call
#   that function with the two numbers, and print the result.

# TODO 6: Ask "Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ".

# TODO 7: On y, keep going from that result. Print the symbols again, ask for the next operation and the next
#   number, run the result through the chosen function, print the new result, and ask y or n again.

# TODO 8: n ends that continuation. The outer loop starts over: logo, a new first number, and a new calculation.

from art import logo
def add(n1, n2):
    """Return the sum of the two numbers."""
    return n1 + n2
def subtract(n1, n2):
    """Return the first number minus the second."""
    return n1 - n2
def multiply(n1, n2):
    """Return the product of the two numbers."""
    return n1 * n2
def divide(n1, n2):
    """Return the first number divided by the second."""
    return n1 / n2
math = {"+": add, "-": subtract, "*": multiply, "/": divide}
reset = False
while not reset:
    print(logo)
    first_number = float(input("What's the first number: "))
    for operation in math:
        print(operation)
    operation = input("Pick an operation: ")
    second_number = float(input("What's the second number: "))
    result = math[operation](first_number, second_number)
    print(result)
    another_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if another_calculation == "y":
        continue_calc = False
        while not continue_calc:
            for operation in math:
                print(operation)
            next_operation = input("Pick an operation: ")
            next_number = float(input("What's the next number: "))
            new_result = math[next_operation](result, next_number)
            print(new_result)
            result = new_result
            another_calculation = input(f"Type 'y' to continue calculating with {new_result}, or type 'n' to start a new calculation: ")
            if another_calculation == "n":
                continue_calc = True

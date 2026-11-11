# TODO 1: Import the logo from art.

# TODO 2: Define addition, subtraction, multiplication, and division. Each takes two numbers, has a docstring,
#   and returns the result.

# TODO 3: Map "+", "-", "*", and "/" to those four functions.

# TODO 4: Define calculator() with a docstring. It prints the logo, asks "What's the first number?: " as a float,
#   and keeps a calculating flag set to True.

# TODO 5: While calculating, print each operation symbol, ask "Pick an operation: " and "What's the second
#   number?: ", call the mapped function, and print the step as "{first} {symbol} {second} = {answer}".

# TODO 6: Ask "Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: " and
#   lowercase the answer.

# TODO 7: On y, set the first number to that answer and keep asking for the next operation and the next number.
#   Print each new step the same way. y again keeps the newest answer as the first number.

# TODO 8: On n, from either question, call calculator() so a new calculation starts from the logo.

from art import logo
def addition(n1, n2):
    """Return the sum of the two numbers."""
    return n1 + n2
def subtraction(n1, n2):
    """Return the first number minus the second."""
    return n1 - n2
def multiplication(n1, n2):
    """Return the product of the two numbers."""
    return n1 * n2
def division(n1, n2):
    """Return the first number divided by the second."""
    return n1 / n2
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
def calculator():
    """Run a calculation, then continue with the result or start over."""
    calculating = True
    print(logo)
    num1 = float(input("What's the first number?: "))
    while calculating:
        for keys in operations:
            print(keys)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if go_again == "y":
            num1 = answer
            while calculating:
                for keys in operations:
                    print(keys)
                operation = input("Pick an operation: ")
                num2 = float(input("What's the second number?: "))
                answer = operations[operation](num1, num2)
                print(f"{num1} {operation} {num2} = {answer}")
                go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
                if go_again == "y":
                    num1 = answer
                else:
                    calculator()
        else:
            calculator()
calculator()

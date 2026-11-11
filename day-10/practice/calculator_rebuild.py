# TODO 1: Define the four operations and map +, -, *, and / to them.
# TODO 2: In calculator(), show the logo and print each step as an equation.
# TODO 3: On y, continue from the last answer. On n, start calculator() over.

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

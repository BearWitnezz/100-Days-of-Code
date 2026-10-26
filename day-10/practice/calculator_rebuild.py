from art import logo
def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
def calculator():
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

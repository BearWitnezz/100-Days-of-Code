from art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
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

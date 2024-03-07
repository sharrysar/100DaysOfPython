from art import logo
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():

    print(logo)
    num1 = float(input("What is the first number? "))
    again = True

    while again:
        for o in operators:
            print(o)
        function = input("Pick an operator from the list. ")
        num2 = float(input("What is the next number? "))
        operation = operators[function]
        answer = operation(num1, num2)

        print(f"{num1} {function} {num2} = {answer}")

        try_again = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation,\nor type 'exit' to exit: "
        )

        if try_again == 'y':
            clear()
            num1 = answer
        elif try_again == 'n':
            again = False
            calculator()
        else:
            again = False


calculator()

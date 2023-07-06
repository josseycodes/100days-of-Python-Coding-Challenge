def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed"
    return num1 / num2

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Available operations: +, -, *, /")
    print("Enter 'q' to quit")

    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator == 'q':
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator!")
            continue

        print("Result: ", result)
        print()

calculator()


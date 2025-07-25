# Basic Calculator Program for PLP Assignment
# Name Muez Gidey Asefa

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == '-':
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("NA: CAN't Devide By zero.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")


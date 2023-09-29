Import the math module for additional functions
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root (Enter 'sqrt')")
    print("6. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
        elif choice == '5':
            num = float(input("Enter a number: "))
            print("Result: ", math.sqrt(num))
        elif choice == '6':
            print("Exiting the Calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

# Call the calculator function to run the program
calculator()
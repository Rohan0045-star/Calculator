def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def floor_div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")


def calculator():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponent (^)")
        print("6. Modulus (%)")
        print("7. Floor Division (//)")
        print("8. Exit")

        choice = input("Choose an operation (1-8): ")

        if choice == "8":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["1","2","3","4","5","6","7"]:
            print("Invalid option. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = power(num1, num2)
        elif choice == "6":
            result = modulus(num1, num2)
        elif choice == "7":
            result = floor_div(num1, num2)

        print(f"Result: {result}")


calculator()

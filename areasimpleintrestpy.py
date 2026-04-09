import math


def compute_area():
    print("\n--- Area Calculation ---")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    choice = input("Choose shape (1/2/3): ").strip()

    try:
        if choice == "1":
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            if length <= 0 or breadth <= 0:
                raise ValueError("Dimensions must be positive.")
            area = length * breadth
            print(f"Area of Rectangle: {area:.2f}")

        elif choice == "2":
            radius = float(input("Enter radius: "))
            if radius <= 0:
                raise ValueError("Radius must be positive.")
            area = math.pi * radius ** 2
            print(f"Area of Circle: {area:.2f}")

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            if base <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive.")
            area = 0.5 * base * height
            print(f"Area of Triangle: {area:.2f}")

        else:
            print("Invalid choice.")

    except ValueError as e:
        print(f"Error: {e}")

# Function to compute simple interest
def compute_simple_interest():
    print("\n--- Simple Interest Calculation ---")
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time (in years): "))

        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Values must be non-negative.")

        si = (principal * rate * time) / 100
        print(f"Simple Interest: {si:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


def basic_arithmetic():
    print("\n--- Basic Arithmetic ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ").strip()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Compute Area")
        print("2. Compute Simple Interest")
        print("3. Basic Arithmetic")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            compute_area()
        elif choice == "2":
            compute_simple_interest()
        elif choice == "3":
            basic_arithmetic()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

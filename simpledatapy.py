

def main():
    try:
        
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            
        age_input = input("Enter your age: ").strip()
        if not age_input.isdigit():
            print("Invalid age. Please enter a positive integer.")
            return
        age = int(age_input)

        
        height_input = input("Enter your height in meters (e.g., 1.75): ").strip()
        try:
            height = float(height_input)
            if height <= 0:
                print("Height must be a positive number.")
                return
        except ValueError:
            print("Invalid height. Please enter a numeric value.")
            return

        
        print(f"\nHello, {name}! You are {age} years old and {height:.2f} meters tall.")

        
        print("Hello, {}! You are {} years old and {:.2f} meters tall.".format(name, age, height))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

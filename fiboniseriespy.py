def fibonacci_series(n):
    """Generate Fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def main():
    try:
        # Take user input
        n = int(input("Enter the number of terms (n): "))
        
        # Validate input
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        elif n == 0:
            print("Fibonacci series: []")
            return
        
        # Generate and display the series
        result = fibonacci_series(n)
        print(f"Fibonacci series of {n} terms: {result}")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

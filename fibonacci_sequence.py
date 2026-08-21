"""
The aim of this program is to efficiently compute the nth Fibonacci number using techniques that
optimize time complexity, ensuring that the computation is fast and scalable even for large values of n.
"""
"""

def fibonacci(n):

    # Check for negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # First two Fibonacci numbers
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Initialize first two values
    a = 0
    b = 1

    # Calculate Fibonacci number
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


# Main program
if __name__ == "__main__":

    print("=" * 45)
    print("       EFFICIENT FIBONACCI CALCULATOR")
    print("=" * 45)

    try:
        n = int(input("Enter position (n): "))

        result = fibonacci(n)

        print("-" * 45)
        print(f"The {n}th Fibonacci number is: {result}")
        print("-" * 45)

    except ValueError:
        print("Error: Please enter a valid non-negative integer.")




=============================================
       EFFICIENT FIBONACCI CALCULATOR
=============================================
Enter position (n): 10
---------------------------------------------
The 10th Fibonacci number is: 55
---------------------------------------------

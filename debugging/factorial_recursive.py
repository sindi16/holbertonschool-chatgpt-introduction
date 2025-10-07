#!/usr/bin/python3
import sys  # Import the sys module to access command-line arguments

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n recursively.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: factorial of n
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Read the first command-line argument, convert it to int, and pass to factorial function
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)

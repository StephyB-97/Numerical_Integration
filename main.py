import math  # Importing the math module to use the sin function

# Define the function to integrate: f(x) = sin(x^2)
def f(x):
    return math.sin(x**2)

# Midpoint Rule
def midpoint_rule(a, b, n):
    """
    Approximates the integral of f(x) over [a, b] using the Midpoint Rule.
    """
    dx = (b - a) / n  # Step size
    total = 0  # Initialize the sum for the integral approximation
    for i in range(n):  # Loop over each subinterval
        x_mid = a + (i + 0.5) * dx  # Midpoint of the current subinterval
        total += f(x_mid)  # Add the function value at the midpoint to the total
    return total * dx  # Multiply the sum by the subinterval width to get the final result

# Trapezoid Rule
def trapezoid_rule(a, b, n):
    """
    Approximates the integral of f(x) over [a, b] using the Trapezoid Rule.
    """
    dx = (b - a) / n  # Step size
    total = (f(a) + f(b)) / 2  # Start with the endpoints contribution
    for i in range(1, n):  # Loop over interior points
        x = a + i * dx  # Calculate the x-coordinate
        total += f(x)  # Add the function value to the total
    return total * dx  # Multiply the sum by the subinterval width

# Simpson's Rule
def simpsons_rule(a, b, n):
    """
    Approximates the integral of f(x) over [a, b] using Simpson's Rule.
    """
    if n % 2 != 0:  # Check if n is even
        raise ValueError("n must be even for Simpson's Rule.")
    dx = (b - a) / n  # Step size
    total = f(a) + f(b)  # Start with the endpoints contribution
    for i in range(1, n, 2):  # Loop over odd-indexed points
        x = a + i * dx
        total += 4 * f(x)  # Multiply odd-indexed terms by 4
    for i in range(2, n, 2):  # Loop over even-indexed points
        x = a + i * dx
        total += 2 * f(x)  # Multiply even-indexed terms by 2
    return total * dx / 3  # Multiply the sum by dx/3

# Given bounds and subinterval counts
a = 0  # Lower bound of the integral
b = 4  # Upper bound of the integral
n_values = [10, 100, 1000]  # Subinterval counts

# Print the results of numerical integration
print("Numerical Integration Results for ∫[0,4] sin(x^2) dx:")
print("-" * 60)

# Loop through each value of n
for n in n_values:
    print(f"n = {n}")  # Indicate the current subinterval count
    print(f"  Midpoint Rule: {midpoint_rule(a, b, n):.6f}")  # Midpoint Rule result
    print(f"  Trapezoid Rule: {trapezoid_rule(a, b, n):.6f}")  # Trapezoid Rule result
    try:
        print(f"  Simpson's Rule: {simpsons_rule(a, b, n):.6f}")  # Simpson's Rule result
    except ValueError as e:
        print(f"  Simpson's Rule: {e}")  # Handle odd n for Simpson's Rule
    print("-" * 60)

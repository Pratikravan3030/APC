def add(a, b):
    """Function to add two numbers."""
    return a + b

def factorial(n):
    """Function to calculate factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = add(5, 3)
print(f"Sum: {result}")

fact = factorial(5)
print(f"Factorial: {fact}")

def greet_with_name(name="Ishaan"):
    print ("Hello, " + name)
greet_with_name()
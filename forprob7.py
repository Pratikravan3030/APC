# Write a short PYTHON program to check whether the square root of a number is prime or not.

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
sqrt_n = math.isqrt(n)

if sqrt_n * sqrt_n != n:
    print("Square root is not a whole number, so cannot check if it's prime.")
else:
    if is_prime(sqrt_n):
        print("The square root is prime.")
    else:
        print("The square root is not prime.")

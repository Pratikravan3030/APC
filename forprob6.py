# Write a PYTHON program to compute the cosine series
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ... up to x^n/n!

import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the value of n (even number): "))
cosine = 0

for i in range(0, n+1, 2):
    term = ((-1)**(i//2)) * (x**i) / math.factorial(i)
    cosine += term

print("cos(x) ≈", cosine)

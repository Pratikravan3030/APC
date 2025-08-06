# Write a PYTHON program to sum the given sequence
# 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!

import math

n = int(input("Enter the value of n: "))
total = 0
for i in range(0, n+1):
    total += 1 / math.factorial(i)
print("Sum of the series is:", total)

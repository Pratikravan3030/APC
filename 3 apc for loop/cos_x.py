import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

cos_x = 0
for i in range(n):
    numerator = (-1)*i * x*(2*i)
    denominator = math.factorial(2*i)
    cos_x += numerator / denominator

print(f"cos({x}) approximated using {n} terms is: {cos_x}")
print(f"Actual math.cos({x}) is: {math.cos(x)}")
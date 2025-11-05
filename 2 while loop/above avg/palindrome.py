n = int(input("Enter a number: "))
original = n
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

if original == reversed_num:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")
    
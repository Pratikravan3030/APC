# Write a PYTHON program that prints 1 2 4 8 16 32 ... up to n

n = int(input("Enter the upper limit: "))
i = 1
while i <= n:
    print(i, end=' ')
    i *= 2

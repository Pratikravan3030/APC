# Write a PYTHON program to produce the following design
# 1
# 12
# 123
# 1234
# 12345
# (If user enters n value as 5)

n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

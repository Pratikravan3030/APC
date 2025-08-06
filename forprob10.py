# Write a PYTHON program to produce the following design
# ABCDE 
# ABCD
# ABC
# AB
# A
# (If user enters n value as 5)

n = int(input("Enter the value of n: "))
for i in range(n, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end='')
    print()

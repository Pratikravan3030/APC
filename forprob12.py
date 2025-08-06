# Write a PYTHON program to produce the following design
# 1
# 22
# 333
# 4444
# 55555
# (If user enters n value as 5)

n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    print(str(i) * i)

n = int(input("Enter the value of n: "))
i=1
for _ in range(1,(n*n)+1):
    if i>=n**2:
        break
    print(i)
    i*=2
print()
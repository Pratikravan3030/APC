import math

num = int(input("Enter a number: "))
root = int(math.sqrt(num))

if root < 2:
    print(f"The square root {root} is not prime.")
else:
    for i in range(2, int(root ** 0.5) + 1):
        if root % i == 0:
            print(f"The square root {root} is not prime.")
            break
    else:
        print(f"The square root {root} is prime.")
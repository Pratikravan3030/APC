n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not a prime number")
else:
    i = 2
    is_prime = True
    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
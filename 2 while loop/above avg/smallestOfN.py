n = int(input("Enter how many numbers: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    smallest = None
    count = 1
    while count <= n:
        num = int(input(f"Enter number {count}: "))
        if smallest is None or num < smallest:
            smallest = num
        count += 1
    print("The smallest number is", smallest)
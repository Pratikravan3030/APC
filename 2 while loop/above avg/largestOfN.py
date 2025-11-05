n = int(input("Enter how many numbers: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    largest = None
    count = 1
    while count <= n:
        num = int(input(f"Enter number {count}: "))
        if largest is None or num > largest:
            largest = num
        count += 1
    print("The largest number is", largest)
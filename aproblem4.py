n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1, 2):
    total += i
print(f"Sum of odd numbers up to {n} is {total}")

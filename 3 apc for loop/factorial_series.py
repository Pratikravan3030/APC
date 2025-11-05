n = int(input("Enter the value of n: "))
print(f"Sum of 1 + 1/1! + 1/2! + 1/3! + ... + 1/{n}! are:")
sum_seq = 1 
fact = 1
for i in range(1, n+1):  
    fact *= i  
    sum_seq += 1/fact
print(sum_seq)
n=int(input("Enter a number: "))
m=int(input("Enter another number: "))
o=int(input("Enter a third number: "))

if n < m and n<o:
    print(f"{n} is the smallest number")

elif m< o and m<n:
    print(f"{m} is the greatest number")

elif o< n and o<m:
    print(f"{o} is the greatest number")
     

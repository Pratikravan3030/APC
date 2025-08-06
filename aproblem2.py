#Write a PYTHON program to find largest of three numbers.


n=int(input("Enter a number: "))
m=int(input("Enter another number: "))
o=int(input("Enter a third number: "))

if n < m and o<m:
    print(f"{m} is the greatest number")

elif n < o and m<o:
    print(f"{o} is the greatest number")

elif m < n and o<n:
    print(f"{n} is the greatest number")
     

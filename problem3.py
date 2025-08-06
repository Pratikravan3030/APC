#Write a PYTHON program that reads the number and check the no is positive or negative.

x=int(input("Enter a number: "))
if x<0:
    print(f"{x} is negative")

elif x>0:
    print(f"{x} is positive")

else:
    print("its zero")
    
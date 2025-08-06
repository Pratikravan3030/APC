#Write a PYTHON program to check entered character is vowel or consonant.

n=str(input("Enter a character: "))

if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
    print(f"{n} is a vowel")

else:
    print(f"{n} is a consonant")
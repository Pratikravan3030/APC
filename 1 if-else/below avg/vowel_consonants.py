vowels=["a","e","i","o","u"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

alphabet=input("Enter an alphabet: ").lower()
if alphabet in vowels:
    print("The entered alphabet is a vowel")
elif alphabet in consonants:
    print("The entered alphabet is a consonant")

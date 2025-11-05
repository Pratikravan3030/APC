class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
d = Dog()
a.speak()  # Output: Animal speaks
d.speak()  # Output: Dog barks
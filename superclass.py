#super key word in python
class A:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"
    
class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name}, aged {self.age}, says hi!"
    
class C(A):
    def __init__(self, name, age, city):
        super().__init__(name)
        self.age = age
        self.city = city

    def speak(self):
        return f"{self.name}, aged {self.age} from {self.city}, says hey!"
    
a1=A("Pratik")
b1=B("Aniket", 21)
c1=C("Sanket", 22, "Pune")
print(a1.speak())
print(b1.speak())
print(c1.speak())
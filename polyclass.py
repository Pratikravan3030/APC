#class polymorphism

class A:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"
    

class B:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hi!"
    
class C:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hey!"

a1=A("Pratik")
b1=B("Aniket")
c1=C("Sanket")
# print(a1.speak())
# print(b1.speak())
# print(c1.speak())

for i in (a1,b1,c1):
    print(i.speak())

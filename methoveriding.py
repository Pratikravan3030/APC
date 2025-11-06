#method overiding
class A:
    def speak(self):
        return "A says hello!"
    
class B(A):
    def speak(self):
        return "B says hi!"
    
class C(A):
    def speak(self):
        return "C says hey!"
    
A=[A(),B(),C()]
for i in A:
    print(i.speak())
#method overloading
class A:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return "No arguments provided"
        
obj = A()
print(obj.add(2, 3, 4))  
print(obj.add(2, 3))     
print(obj.add(2))        
print(obj.add())         
        

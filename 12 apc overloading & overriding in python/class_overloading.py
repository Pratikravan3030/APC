class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0

calc = Calculator()
print(calc.add(2, 3))        # Output: 5
print(calc.add(1, 2, 3))     # Output: 6
print(calc.add(7))           # Output: 7
print(calc.add())            # Output: 0
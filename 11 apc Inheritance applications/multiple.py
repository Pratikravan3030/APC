class Engine:
    def show(self):
        print("This is an Engine")

class Wheels:
    def show(self):
        print("These are Wheels")

class Car(Engine, Wheels):
    def show(self):
        super().show()
        print("This is a Car")

print("Multiple Inheritance:")
car = Car()
car.show()

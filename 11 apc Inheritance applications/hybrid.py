class Vehicle:
    def info(self):
        print("This is a Vehicle")

class Sedan(Vehicle):
    def info(self):
        super().info()
        print("This is a Sedan")

class SUV(Vehicle):
    def info(self):
        super().info()
        print("This is an SUV")

class HybridCar(Sedan, SUV):
    def info(self):
        super().info()
        print("This is a Hybrid Car")

print("\nHybrid Inheritance Example with Car Models:")
car = HybridCar()
car.info()

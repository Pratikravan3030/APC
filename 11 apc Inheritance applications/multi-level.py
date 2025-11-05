class CarBrand:
    def display(self):
        print("The Car Brand is Toyota")

class CarModel(CarBrand):
    def display(self):
        super().display()
        print("The Car Model is Supra")

class CarVariant(CarModel):
    def display(self):
        super().display()
        print("The Car Variant is GR")

print("\nMulti-level Inheritance (Cars Example):")
variant = CarVariant()
variant.display()

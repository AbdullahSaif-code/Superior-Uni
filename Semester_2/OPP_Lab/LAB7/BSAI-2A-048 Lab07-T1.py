class Vehicle():
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}")
class Car(Vehicle):
    def __init__(self, make, model,num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    def additional_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nNumber of Doors: {self.num_doors}")
class LuxuryCar(Car):
    def __init__(self, make, model, num_doors,features):
        super().__init__(num_doors, make, model)
        self.features = features
    def additional_info(self):
                print(f"Make: {self.make}\nModel: {self.model}\nNumber of Doors: {self.num_doors}\nFeatures: {self.features}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
vehicle = Vehicle("Toyota", "Supra")
vehicle.display_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
car = Car("Volkswagen Beetle", "1980", 2)
car.display_info()
car.additional_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

luxury_car = LuxuryCar("Doge Charger R/T", "1969", 2,  "Tribute")
luxury_car.display_info()
luxury_car.additional_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
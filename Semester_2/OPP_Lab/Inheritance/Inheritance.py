# Singale inharitance

class vehicle:
    def __init__(self, make):
        self.make = make
class car(vehicle):
    def __init__(self, model,make,car_engion,doors):
        self.model = model
        super().__init__(make)
        self.car_engion = car_engion
        self.doors = doors
    def printdetails(self):
        print(f"""Make: {self.model}
Model: {self.make}
Car Engion: {self.car_engion}
Doors: {self.doors}""")

mycar = car("Honda" , "Supra 1994 MK4" , "5000HP" , "2")
mycar.printdetails()
# Make: 1998 Supra Mk4
# Model : Honda
# Engion: 5000HP
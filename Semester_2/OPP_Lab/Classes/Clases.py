# What is Classe ?
# Ans: Clases are such as person(Human).It contains functions and templets that works as blue prit.
# Whta is Object?
# Ans: object are the values of class that hold data.

# Class

class kuchBhi:
    pass


class Vehicle:
    def str(self):
        print("Hellow form lol Cars:")
    def __init__(self):    # Constor / Function
        self.str()
        self.x = input("Ente your Name:")
        self.y = input("Ente Car name: ")
        self.z=input("Enter Car Modle: ")
    def printVeh(self):    # meathods / to define function
        print(f"Hellow {self.x}.You buy {self.y} modle {self.z}.")
    def choice(self):
        self.c=int(input("Enter 1 for Yes and 0 for No: "))
        if self.c ==1:
            print("Thanks for our servises")
        else:
            print("Chaly jay ******.")

Car = Vehicle()
Car.printVeh()
Car.choice()
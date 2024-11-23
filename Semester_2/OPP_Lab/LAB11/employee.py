class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    # Getter and Setter
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

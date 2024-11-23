# Parent calass
from employee import Employee

# Child class
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    # Getter and Setter
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department
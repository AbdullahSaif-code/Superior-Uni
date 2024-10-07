class Employee():
    def __init__(self,name,postion):
        self.name = name
        self.postion = postion
    
    def  display_info(self):
        print(f"Name: {self.name}\nPostion: {self.postion}")
class Manager(Employee):
    def __init__(self, name, postion,departmentOfmanger):
        super().__init__(name, postion)
        self.departmentOfmanger = departmentOfmanger
    def additional_info(self):
        print(f"Name: {self.name}\nPostion: {self.postion}\nDepart of Manger: {self.departmentOfmanger}")
class Worker(Employee):
    def __init__(self, name, postion, hours_worked):
        super().__init__(name, postion)
        self.hours_worked =  hours_worked
    def additional_info(self):
        print(f"Name: {self.name}\nPostion: {self.postion}\nWorking Hours: {self.hours_worked}")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
employee = Employee("Rasik", "Teacher")
employee.display_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
manager = Manager("Rasik Ali", "Teacher", "Python Lab")
manager.additional_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
worker = Worker("Abdullah Saif", "Student", 8)
worker.additional_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
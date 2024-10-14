# Main funcation to run whole code for first time.
def main():
    class Person: # Person class for personal details.
        def info(self, name, age):
            self.name = name
            self.age = age
        def display_info(self):
            print(f"Name: {self.name}\nAge: {self.age}")
    class Employee: # Employee class for profeasional details.
        def info(self, emp_id, position):
            self.emp_id = emp_id
            self.position = position
        def display_info(self):
            print(f"Employee ID: {self.emp_id}\nPosition: {self.position}")
    class Staff(Person, Employee): # Staff class for all details and printing it.
        def __init__(self, name, age, emp_id, position, department):
            Person.info(self, name, age)
            Employee.info(self, emp_id, position)
            self.department = department
        def display_info(self):
            Person.display_info(self)
            Employee.display_info(self)
        def additional_info(self):
            print(f"Department: {self.department}")
    # Input for program.
    staff_input = Staff(input("Enter Name: ").upper(),input("Enter Age: "),input("Enter ID: "),input("Enter Position: ").upper(),input("Enter Department: ").upper())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    staff_input.display_info()
    staff_input.additional_info()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # CSV file handling with extra functions.
    import os
    import csv
    def read_employee(file_CSV):
        employees = []
        with open(file_CSV, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:
                    employees.append(Staff(row[0], (row[1]), row[2], row[3], row[4]))
        return employees
    # Add new employee data.
    def add_employee(file_CSV, staff):
        with open(file_CSV, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([staff.name, staff.age, staff.emp_id, staff.position, staff.department])
    # Save data in CSV.
    def save_employees(file_CSV, employees):
        with open(file_CSV, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            for staff in employees:
                csv_writer.writerow([staff.name, staff.age, staff.emp_id, staff.position, staff.department])
    file_CSV = "employees.csv"
    # Run Add Employee.
    add_employee(file_CSV, staff_input)
    employees = read_employee(file_CSV)
    # While loop for Menu.
    while True:
        value = input(f"Enter\n'N' to new data entery\n'O' to open in Excel\n'P' to print from CSV\n'Q' to quite\nWating Comand: ")
        value = value.upper()
        print("~~~~~~~~~~~~~~~~~~~")
        if value == "N": # For new data input.
            print("~~~~~~~~~~~~~~~~~~~")
            main()
        elif value == "O": # Opne extrnal CSV.
            os.startfile(file_CSV)
        elif value == "P": # Print data in terminal.
            print("~~~~~~~~~~~~~~~~~~~")
            for emp in employees:
                emp.display_info()
                emp.additional_info()
                save_employees(file_CSV, employees)
                print("~~~~~~~~~~~~~~~~~~~")
        elif value =="Q": # Quit.
            print("~~~~~~~~~~~~~~~~~~~")
            print("Thanks to use Sir.")
            break
        else:
            print("Enter Corect option.")
main() # Calling main function for first run. 
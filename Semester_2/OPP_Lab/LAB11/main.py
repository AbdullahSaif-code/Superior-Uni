import csv
import os

# Parent class
from employee import Employee

# Child class
from manager import Manager

# Child class
from worker import Worker

# File handling
def save_employee(filename, data, headers):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if os.stat(filename).st_size == 0:
            writer.writerow(headers)
        writer.writerow(data)
    print(f"Data saved to {filename}")

def read_employees(filename):
    if not os.path.exists(filename):
        print(f"No data found in {filename}.")
        return []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, [])
        data = [row for row in reader if row]
        return headers, data

def update_csv(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Data updated in {filename}")

# Main menu
def menu():
    filename = "employees.csv"
    while True:
        print("\nChoose the options:")
        print("1: Add Manager")
        print("2: Add Worker")
        print("3: View All Employees")
        print("4: Update Employee Information")
        print("5: Delete Employee")
        print("6: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter manager's name: ")
            age = input("Enter manager's age: ")
            salary = input("Enter manager's salary: ")
            department = input("Enter manager's department: ")
            manager = Manager(name, age, salary, department)
            save_employee(filename, [manager.name, manager.get_age(), manager.get_salary(), manager.get_department(), "---"],
                          ["Name", "Age", "Salary", "Department", "Hours Worked"])
        
        elif choice == "2":
            name = input("Enter worker's name: ")
            age = input("Enter worker's age: ")
            salary = input("Enter worker's salary: ")
            hours_worked = input("Enter worker's hours worked: ")
            worker = Worker(name, age, salary, hours_worked)
            save_employee(filename, [worker.name, worker.get_age(), worker.get_salary(), "---", worker.get_hours_worked()],
                          ["Name", "Age", "Salary", "Department", "Hours Worked"])
        
        elif choice == "3":
            csv_file_name = "employees.csv"
            if os.path.exists(csv_file_name):
                print(f"Opening {csv_file_name}")
                os.startfile(csv_file_name)
            else:
                print("No CSV file found.")
        
        elif choice == "4":
            headers, data = read_employees(filename)
            if data:
                emp_name = input("Enter the name to update: ")
                employee_found = False
                for row in data:
                    if row[0] == emp_name:
                        employee_found = True
                        print(f"Current details: {', '.join(row)}")
                        field = input(f"Select field to update ({', '.join(headers)}): ")
                        if field in headers:
                            value = input(f"Enter new value for {field}: ")
                            row[headers.index(field)] = value
                            update_csv(filename, [headers] + data)
                            print("Employee information updated.")
                        else:
                            print("Invalid name.")
                        break
                if not employee_found:
                    print(f"Employee with name '{emp_name}' not found.")
            else:
                print("No employees to update.")

        elif choice == "5":
            headers, data = read_employees(filename)
            if data:
                emp_name = input("Enter the name to delete: ")
                new_data = [row for row in data if row[0] != emp_name]
                if len(new_data) < len(data):
                    update_csv(filename, [headers] + new_data)
                    print(f"Employee '{emp_name}' deleted successfully.")
                else:
                    print(f"Employee with name '{emp_name}' not found.")
            else:
                print("No employees to delete.")

        
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()

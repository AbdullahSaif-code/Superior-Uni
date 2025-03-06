class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        priorities = ["High", "Medium", "Low"]
        return f"{self.description} (Priority: {priorities[self.priority - 1]})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        if priority in [1, 2, 3]:
            self.tasks.append(Task(description, priority))
            self.tasks = sorted(self.tasks, key=lambda x: x.priority)  # Lamda function is used to provide small anomyas feature.
            print("Task added.")
        else:
            print("Invalid priority.")

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            print(f"{self.tasks.pop(task_number - 1).description} removed.")
        else:
            print("Invalid number.")

    def run(self):
        while True:
            print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
            choice = input("Choice: ")
            if choice == "1":
                desc = input("Description: ")
                prio = int(input("Priority (1: High, 2: Medium, 3: Low): "))
                self.add_task(desc, prio)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                num = int(input("Task number: "))
                self.delete_task(num)
            elif choice == "4":
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")

ToDoList().run() # Calling class and than function short hand stecture same as used in pandas asnd numpy.

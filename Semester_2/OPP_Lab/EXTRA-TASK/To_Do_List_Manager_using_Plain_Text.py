import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            for line in file:
                task, completed = line.strip().split(" | ")
                tasks.append({"task": task, "completed": completed == "True"})
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['completed']}\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as completed!")
    else:
        print("Invalid task number.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Your to-do list is empty!")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✖"
        print(f"{i}. {task['task']} [{status}]")

def main():
    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Mark task as completed")
        print("3. List all tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            complete_task(task_number)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

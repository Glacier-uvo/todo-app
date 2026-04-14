Print("B version Local verison running")
Print("A version Teammate v2")
Print("B version Local verison running before Teammate owner")
 337c8f65abe520f37cbbbeaebfce746a2a5e62cd
8e6ccbc12478d78c45385ab6c69df8eab2b8a130

FILE = "tasks.txt"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid choice.")

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid option")


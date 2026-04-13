tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
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

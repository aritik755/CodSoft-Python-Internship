todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})

def view_tasks():
    print("\n--- Tasks ---")
    for i, task in enumerate(todo_list):
        status = "✔" if task["done"] else "✖"
        print(f"{i+1}. [{status}] {task['task']}")

def mark_task_complete():
    view_tasks()
    num = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= num < len(todo_list):
        todo_list[num]["done"] = True
    else:
        print("Invalid task number!")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: ")) - 1
    if 0 <= num < len(todo_list):
        todo_list.pop(num)
    else:
        print("Invalid task number!")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

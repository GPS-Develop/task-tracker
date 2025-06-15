import task



tasks = task.load_tasks()

def display_menu():
    print("\nTask Tracker")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Quit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task.view_all_tasks(tasks)
    elif choice == "2":
        task.add_task(tasks)
    elif choice == "3":
        task.mark_as_complete(tasks)
    elif choice == "4":
        print("Deleting task... (to be implemented)")
    elif choice == "5":
        print("Exiting Task Tracker.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
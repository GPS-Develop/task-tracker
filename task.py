import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    name = input("Enter task name: ").strip()
    if not name:
        print("Task name cannot be empty.")
        return

    while True:
        due_date_input = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date().isoformat()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        is_done_input = input("Is the task done? (y/n): ").strip().lower()
        if is_done_input in ["y", "n"]:
            is_done = is_done_input == "y"
            break
        else:
            print("Please enter 'y' or 'n'.")

    task = {
        "name": name,
        "due_date": due_date,
        "is_done": is_done
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def no_task(tasks,message):
        if not tasks:
            print(message)
            return True
        return False

def view_all_tasks(tasks):
    no_task(tasks, "No tasks to view")
    for i, task in enumerate(tasks, start=1):
        if task["is_done"] is True:
            check_or_cross = "✅"
        else:
            check_or_cross = "❌"    
        print(f'{i}. {task["name"]} - due {task["due_date"]} - {check_or_cross}')

def validate_digit(choice, tasks):
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return    
    return index


def mark_as_complete(tasks):
    if no_task(tasks, "No Tasks to mark Complete"):
        return
    view_all_tasks(tasks)
    choice = input("Enter the number of the task to mark complete: ")
    index = validate_digit(choice, tasks)
    
    if tasks[index]["is_done"]:
        print(f"Task '{tasks[index]['name']}' is already marked as complete.")
        return
    
    tasks[index]["is_done"] = True
    save_tasks(tasks)
    print(f'✅ {tasks[index]["name"]} marked as complete.')   


def delete_task(tasks):
    if no_task(tasks, "No tasks to delete."):
        return

    view_all_tasks(tasks)
    choice = input("Enter the number of the task to delete: ")
    index = validate_digit(choice, tasks)

    if index is None:
        return

    deleted_name = tasks[index]["name"]
    del tasks[index]
    save_tasks(tasks)
    print(f'🗑️ "{deleted_name}" has been deleted.')



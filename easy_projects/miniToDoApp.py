import json
import os

TASK_FILE = "tasks.json"
VALID_STATUS = {"incompleted", "completed"}

def init_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

def load_tasks():
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

def normalize_status(raw: str) -> str | None:
    s = raw.strip().lower()
    if s in {"c", "completed", "done", "finish", "finished"}:
        return "completed"
    if s in {"p", "pending", "incomplete", "not done", "open"}:
        return "incompleted"
    if s in VALID_STATUS:
        return s
    return None

def add_task(task):
    task = task.strip()
    if not task:
        print("Task cannot be empty.")
        return

    tasks = load_tasks()
    tasks.append({"task": task, "status": "incompleted"})
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks=None):
    if tasks is None:
        tasks = load_tasks()

    if tasks:
        print("\n--- To-Do List ---")
        for idx, t in enumerate(tasks, 1):
            print(f"{idx}. {t['task']} - {t['status']}")
    else:
        print("No tasks found.")

def update_status():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return

    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            raw = input("Enter new status (incompleted/completed): ")
            new_status = normalize_status(raw)
            if new_status is None:
                print("Invalid status. Use 'incompleted' or 'completed'.")
                return

            tasks[task_index]["status"] = new_status
            save_tasks(tasks)
            print("Task status updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Deleted: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def display_menu():
    print("\n--- Mini To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

def main():
    init_file()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
            view_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the app. Goodbye!:)")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
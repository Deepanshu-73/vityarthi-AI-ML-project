import json

FILE = "tasks.json"

# Load tasks
def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task(tasks):
    name = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()

    task = {
        "name": name,
        "priority": priority,
        "done": False
    }

    tasks.append(task)
    print("✅ Task added!")

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    # Priority order
    order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: order.get(x["priority"], 4))

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "❌"
        print(f"{i+1}. {task['name']} [{task['priority']}] {status}")

# Mark complete
def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1]["done"] = True
        print("🎉 Task completed!")
    except:
        print("Invalid input")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("🗑 Task deleted!")
    except:
        print("Invalid input")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== STUDY PLANNER =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Saved! Goodbye!")
            break
        else:
            print("Invalid choice")

main()

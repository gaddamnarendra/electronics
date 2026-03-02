def show_tasks():
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter new task: ")
        add_task(task)
    elif choice == "3":
        break
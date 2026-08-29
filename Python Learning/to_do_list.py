tasks = []

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("There are no tasks to remove.")
            continue

        for number, task in enumerate(tasks, 1):
            print(f"{number}. {task}")

        try:
            number = int(input("Enter task number: "))
            removed = tasks.pop(number - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
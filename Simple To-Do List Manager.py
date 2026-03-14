tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(i, ".", t)

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)

    elif choice == "4":
        break
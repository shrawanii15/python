expenses = []
total = 0

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        total = sum(expenses)
        print("Total Expense:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
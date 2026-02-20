print("Welcome to Fun Café")

print("1. Coffee - 50")
print("2. Tea - 30")
print("3. Sandwich - 70")

choice = int(input("Enter item number: "))
qty = int(input("Enter quantity: "))

if choice == 1:
    total = 50 * qty
elif choice == 2:
    total = 30 * qty
elif choice == 3:
    total = 70 * qty
else:
    total = 0
    print("Invalid choice")

print("Total Bill =", total)
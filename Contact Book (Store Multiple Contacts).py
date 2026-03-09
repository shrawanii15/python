contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved!")

    elif choice == "2":
        print("\nContact List:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
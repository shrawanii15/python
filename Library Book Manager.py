books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added!")

    elif choice == "2":
        print("\nAvailable Books:")
        for b in books:
            print("-", b)

    elif choice == "3":
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed")
        else:
            print("Book not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
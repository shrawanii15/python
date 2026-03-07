source = input("Enter source file name: ")
destination = input("Enter destination file name: ")
try:
    with open(source, "r") as file1:
        lines = file1.readlines()
    with open(destination, "w") as file2:
        for line in lines:
            if not line.strip().startswith("#"):
                file2.write(line)
    print("\nSource File Content")
    with open(source, "r") as file1:
        print(file1.read())
    print("\n Destination File Content (Without Comments)")
    with open(destination, "r") as file2:
        print(file2.read())
except FileNotFoundError:
    print("Source file not found!")
# Base class
class Employee:
    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display_data(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)



class Manager(Employee):
    def get_manager_data(self):
        print("\nEnter Manager Details:")
        self.get_data()   # calling parent method

    def display_manager_data(self):
        print("\n Manager Details ")
        self.display_data()   # calling parent method



managers = []

for i in range(10):
    print(f"\nManager {i+1}:")
    m = Manager()
    m.get_manager_data()
    managers.append(m)


print("\n  All Manager Details ")

for m in managers:
    m.display_manager_data()
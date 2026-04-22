import pandas as pd

df = pd.read_csv("employee.csv")

# a) Automotive employees
print("\nAutomotive Employees:")
print(df[df["Department"] == "Automotive"])

# b) Search by ID
emp_id = int(input("\nEnter Employee ID: "))
print(df[df["EmployeeID"] == emp_id])

# c) Developers
print("\nDevelopers:")
print(df[df["Designation"] == "Developer"])
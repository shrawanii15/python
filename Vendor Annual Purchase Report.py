name = input("Vendor Name: ")
year = input("Year of Association: ")
contact = input("Contact Number: ")
email = input("Email ID: ")
total = 0
print("\nEnter monthly purchase amounts:")
for i in range(1, 13):
    purchase = float(input("Month " + str(i) + ": "))
    total = total + purchase
print("\n----- Annual Billing Report -----")
print("Vendor:", name)
print("Associated Since:", year)
print("Contact:", contact)
print("Email:", email)
print("Total Annual Purchase:", total)
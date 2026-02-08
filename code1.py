# Student Marksheet Program (Beginner Level)


name = input("Enter student name: ")
department = input("Enter department: ")
year = input("Enter year: ")
semester = input("Enter semester: ")
section = input("Enter section: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks of 5 subjects:")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total_marks / 5


print("\n------ STUDENT MARKSHEET ------")
print("Name:", name)
print("Department:", department)
print("Year:", year)
print("Semester:", semester)
print("Section:", section)
print("Roll Number:", roll_no)

print("\nMarks Obtained:")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)

print("\nTotal Marks:", total_marks)
print("Percentage:", percentage, "%")


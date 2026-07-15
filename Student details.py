students = {}

while True:
    print("\n***** STUDENT MANAGEMENT SYSTEM *****")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists.")
        else:
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            students.update({roll: {"Name": name, "Marks": marks}})
            print("Student Added Successfully.")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Details")
            for roll, details in students.items():
                print("Roll No:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])
                print("----------------------")

    elif choice == 3:
        roll = input("Enter Roll Number: ")

        student = students.get(roll)

        if student:
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
        else:
            print("Student Not Found.")

    elif choice == 4:
        roll = input("Enter Roll Number: ")

        if roll in students:
            marks = float(input("Enter New Marks: "))
            students[roll]["Marks"] = marks
            print("Marks Updated Successfully.")
        else:
            print("Student Not Found.")

    elif choice == 5:
        roll = input("Enter Roll Number: ")

        if roll in students:
            students.pop(roll)
            print("Student Deleted Successfully.")
        else:
            print("Student Not Found.")

    elif choice == 6:
        if len(students) == 0:
            print("No students found.")
        else:
            topper_roll = max(students, key=lambda x: students[x]["Marks"])

            print("Topper Details")
            print("Roll No:", topper_roll)
            print("Name:", students[topper_roll]["Name"])
            print("Marks:", students[topper_roll]["Marks"])

    elif choice == 7:
        if len(students) == 0:
            print("No students found.")
        else:
            total = 0

            for student in students.values():
                total += student["Marks"]

            average = total / len(students)
            print("Average Marks =", average)

    elif choice == 8:
        print("Total Students =", len(students))

    elif choice == 9:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
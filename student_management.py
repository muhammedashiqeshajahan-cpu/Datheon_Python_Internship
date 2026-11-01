students = []

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Student Name: ")
        roll = input("Roll Number: ")
        course = input("Course: ")

        student = {
            "name": name,
            "roll": roll,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        for student in students:
            print(student)

    elif choice == "3":
        search = input("Enter Roll Number: ")

        for student in students:
            if student["roll"] == search:
                print("Student Found:", student)
                break
        else:
            print("Student not found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

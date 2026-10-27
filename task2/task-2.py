students = []
events = []
resources = [
    ["Library", 100],
    ["Computer Lab", 40],
    ["Seminar Hall", 50]
]

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add Student Record")
    print("2. Mark Attendance")
    print("3. Enter Student Marks")
    print("4. Register for Event")
    print("5. Allocate Campus Resource")
    print("6. Display Student Records")
    print("7. Summary Report")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")

        found = False
        for student in students:
            if student[0] == roll:
                found = True
                break

        if found:
            print("Roll number already exists!")
        else:
            student = [roll, name, department, 0, 0, []]
            students.append(student)
            print("Student record added successfully!")
    elif choice == "2":
        roll = input("Enter Roll Number: ")
        found = False

        for student in students:
            if student[0] == roll:
                status = input("Enter attendance (P/A): ").upper()

                if status == "P":
                    student[3] += 1
                    print("Attendance marked Present.")
                elif status == "A":
                    student[4] += 1
                    print("Attendance marked Absent.")
                else:
                    print("Invalid attendance status!")

                found = True
                break

        if not found:
            print("Student not found!")
    elif choice == "3":
        roll = input("Enter Roll Number: ")
        found = False

        for student in students:
            if student[0] == roll:
                marks = float(input("Enter marks out of 100: "))

                if 0 <= marks <= 100:
                    student[5] = [marks]
                    print("Marks saved successfully!")
                else:
                    print("Marks must be between 0 and 100.")

                found = True
                break

        if not found:
            print("Student not found!")
    elif choice == "4":
        roll = input("Enter Roll Number: ")
        found = False

        for student in students:
            if student[0] == roll:
                event_name = input("Enter Event Name: ")

                registration = (roll, student[1], event_name)
                events.append(registration)

                print("Event registration successful!")
                found = True
                break

        if not found:
            print("Student not found!")
    elif choice == "5":
        print("\nAvailable Campus Resources:")

        for resource, capacity in resources:
            print(resource, "- Capacity:", capacity)

        resource_name = input("Enter Resource Name: ").lower()
        found = False

        for resource, capacity in resources:
            if resource.lower() == resource_name:
                number = int(input("Enter number of students: "))

                if 0 < number <= capacity:
                    print("Resource allocated successfully!")
                else:
                    print("Invalid number or capacity exceeded.")

                found = True
                break

        if not found:
            print("Resource not found!")
    elif choice == "6":
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\n--- Student Records ---")

            for roll, name, department, present, absent, marks in students:
                print("Roll Number:", roll)
                print("Name:", name)
                print("Department:", department)
                print("Present Days:", present)
                print("Absent Days:", absent)

                if len(marks) > 0:
                    print("Marks:", marks[0])
                else:
                    print("Marks: Not entered")

                print("----------------------")
    elif choice == "7":
        print("\n===== CAMPUS SUMMARY REPORT =====")
        print("Total Students:", len(students))
        print("Total Event Registrations:", len(events))

        if len(students) > 0:
            total_marks = 0
            marks_count = 0

            for student in students:
                if len(student[5]) > 0:
                    total_marks += student[5][0]
                    marks_count += 1

            if marks_count > 0:
                average = total_marks / marks_count
                print("Average Marks:", round(average, 2))
            else:
                print("No marks entered yet.")

            print("\nAttendance Summary:")
            for student in students:
                roll, name, department, present, absent, marks = student
                total_days = present + absent

                if total_days > 0:
                    percentage = (present / total_days) * 100
                else:
                    percentage = 0

                print(name, "- Attendance:",
                      round(percentage, 2), "%")

        print("\nEvent Registrations:")
        if len(events) == 0:
            print("No event registrations.")
        else:
            for roll, name, event_name in events:
                print(name, "registered for", event_name)
    elif choice == "8":
        print("Thank you for using Smart Campus Management!")
        break

    else:
        print("Invalid choice! Please enter 1 to 8.")

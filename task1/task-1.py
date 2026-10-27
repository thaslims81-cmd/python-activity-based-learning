MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nEnter details of applicant {i + 1}")

    name = input("Student name: ")
    roll_no = input("Roll number: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input(f"Enter marks for subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / len(marks)

    # Check eligibility criteria
    if (aggregate >= MIN_AGGREGATE
            and all(m >= MIN_SUBJECT_MARKS for m in marks)
            and attendance >= MIN_ATTENDANCE
            and income <= MAX_INCOME):

        applicants.append({
            "name": name,
            "roll_no": roll_no,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        print(name, "is NOT eligible for scholarship.")
applicants.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["roll_no"]
    )
)

# Display final ranking
print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if applicants:
    for rank, student in enumerate(applicants, start=1):
        print(f"\nRank: {rank}")
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Aggregate Marks:", round(student["aggregate"], 2))
        print("Attendance:", student["attendance"], "%")
        print("Family Income:", student["income"])
else:
    print("No eligible applicants found.")

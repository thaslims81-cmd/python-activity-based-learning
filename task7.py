answer_key = ["A", "B", "C", "D", "A"]
students = {
    "Student 1": ["A", "B", "C", "A", "A"],
    "Student 2": ["A", "C", "C", "D", "B"],
    "Student 3": ["B", "B", "C", "D", "A"],
    "Student 4": ["A", "B", "D", "C", "A"]
}

total_questions = len(answer_key)
total_students = len(students)
correct_count = [0] * total_questions
print("STUDENT RESULTS")
print("-" * 40)

for name, answers in students.items():
    score = 0

    for i in range(total_questions):
        if answers[i].upper() == answer_key[i]:
            score += 1
            correct_count[i] += 1

    print(name, ":", score, "/", total_questions)
success_rates = []

print("\nQUESTION-WISE PERFORMANCE")
print("-" * 40)

for i in range(total_questions):
    rate = (correct_count[i] / total_students) * 100
    success_rates.append(rate)

    missed = total_students - correct_count[i]

    if rate >= 80:
        category = "Excellent"
    elif rate >= 60:
        category = "Good"
    elif rate >= 40:
        category = "Average"
    else:
        category = "Poor"

    print("Question", i + 1)
    print("Correct answers:", correct_count[i])
    print("Incorrect answers:", missed)
    print("Success rate:", round(rate, 2), "%")
    print("Classification:", category)
    print()
max_missed = max(
    total_students - count for count in correct_count
)

print("MOST FREQUENTLY MISSED QUESTIONS:")

for i in range(total_questions):
    missed = total_students - correct_count[i]

    if missed == max_missed:
        print("Question", i + 1,
              "- Missed by", missed, "students")

print("\nAnalysis completed.")

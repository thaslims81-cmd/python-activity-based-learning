students = [
    ("S101", "Boys", "CSE"),
    ("S102", "Boys", "CSE"),
    ("S103", "Girls", "ECE"),
    ("S104", "Girls", "CSE"),
    ("S105", "Boys", "ECE"),
    ("S106", "Girls", "ECE"),
    ("S107", "Boys", "CSE")
]
rooms = [
    ("R101", 3, "Boys"),
    ("R102", 2, "Girls"),
    ("R103", 2, "Boys"),
    ("R104", 2, "Girls")
]

assignments = {}
room_occupancy = {}
allocated_students = set()
duplicate_assignments = []
for room in rooms:
    room_occupancy[room[0]] = []
for student in students:
    sid, group, department = student
    allocated = False

    for room in rooms:
        rid, capacity, allowed_group = room
        if group == allowed_group and len(room_occupancy[rid]) < capacity:
            if all(s[2] == department
                   for s in room_occupancy[rid]):

                # Check duplicate assignment
                if sid in allocated_students:
                    duplicate_assignments.append(sid)
                else:
                    room_occupancy[rid].append(student)
                    assignments[sid] = rid
                    allocated_students.add(sid)

                allocated = True
                break

    if not allocated:
        print("Student", sid, "could not be allocated.")
student_ids = [student[0] for student in students]
seen = set()

for sid in student_ids:
    if sid in seen:
        if sid not in duplicate_assignments:
            duplicate_assignments.append(sid)
    seen.add(sid)
unallocated = len(students) - len(allocated_students)
print("\n--- ROOM ALLOCATION REPORT ---")

for room in rooms:
    rid = room[0]
    capacity = room[1]
    occupants = room_occupancy[rid]

    print("\nRoom:", rid)
    print("Capacity:", capacity)
    print("Allocated:", len(occupants))

    for student in occupants:
        print("Student ID:", student[0],
              "Group:", student[1],
              "Department:", student[2])

    print("Vacant Seats:", capacity - len(occupants))

print("\n--- SUMMARY ---")
print("Total Students:", len(students))
print("Allocated Students:", len(allocated_students))
print("Unallocated Demand:", unallocated)
print("Duplicate Assignments:", duplicate_assignments)

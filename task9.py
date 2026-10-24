wards = [
    ["General", 20, 18, 5, 4, 10, 8],
    ["ICU", 10, 10, 6, 3, 8, 5],
    ["Emergency", 15, 12, 4, 2, 6, 4],
    ["Pediatrics", 12, 8, 4, 4, 5, 5]
]

cases = [
    ["Patient A", "ICU", 5],
    ["Patient B", "Emergency", 4],
    ["Patient C", "General", 2],
    ["Patient D", "ICU", 3],
    ["Patient E", "Pediatrics", 1]
]

print("HOSPITAL WARD RESOURCE ANALYSIS")
print("-" * 50)

shortage_count = 0

for ward in wards:
    name = ward[0]
    total_beds = ward[1]
    occupied_beds = ward[2]
    required_staff = ward[3]
    available_staff = ward[4]
    required_equipment = ward[5]
    available_equipment = ward[6]

    vacant_beds = total_beds - occupied_beds
    staff_shortage = max(0, required_staff - available_staff)
    equipment_shortage = max(
        0, required_equipment - available_equipment
    )

    print("\nWard:", name)
    print("Vacant beds:", vacant_beds)
    print("Staff shortage:", staff_shortage)
    print("Equipment shortage:", equipment_shortage)

    if vacant_beds == 0 or staff_shortage > 0 or equipment_shortage > 0:
        print("Status: RESOURCE SHORTAGE")
        shortage_count += 1
    else:
        print("Status: Resources Available")

print("\nTotal wards with shortages:", shortage_count)

cases.sort(key=lambda case: case[2], reverse=True)

print("\nCASE PRIORITY LIST")
print("-" * 50)

for case in cases:
    print("Case:", case[0],
          "| Ward:", case[1],
          "| Priority Score:", case[2])

print("\nHighest priority case:", cases[0][0])

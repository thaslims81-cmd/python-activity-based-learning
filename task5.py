
import re
registrations = [
    "REG001,Ali,ali@gmail.com,9876543210",
    "REG002,John,john@gmail.com,9876543211",
    "REG003,Ravi,ravi@gmail.com,9876543212",
    "REG001,Sam,sam@gmail.com,9876543213",
    "REG005,A,invalidemail,12345",
    "REG006,David,david@gmail.com,9876543214",
    "REG007,Anu,anu@gmail.com,9876543215"
]

seen_ids = set()

for record in registrations:
    print("\nRegistration:", record)
    fields = record.split(",")
    if len(fields) != 4:
        print("Error: Incorrect number of fields")
        continue

    reg_id, name, email, phone = fields

    errors = []
    if not re.fullmatch(r"REG\d{3}", reg_id):
        errors.append("Invalid registration ID format")
    if len(name) < 2 or len(name) > 30:
        errors.append("Name length must be 2 to 30 characters")
    if not re.fullmatch(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        email
    ):
        errors.append("Invalid email format")
    if not re.fullmatch(r"\d{10}", phone):
        errors.append("Phone number must contain 10 digits")
    if reg_id in seen_ids:
        errors.append("Duplicate registration ID")
    else:
        seen_ids.add(reg_id)
    print("Registration ID:", reg_id)
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    if errors:
        print("Status: INVALID")
        for error in errors:
            print("Error:", error)
    else:
        print("Status: VALID")

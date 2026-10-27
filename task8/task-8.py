accounts = {
    "A101": 5000,
    "A102": 3000,
    "A103": 4000
}

transactions = [
    ("DEPOSIT", "A101", 1000, ""),
    ("WITHDRAW", "A101", 2000, ""),
    ("TRANSFER", "A101", 1500, "A102"),
    ("WITHDRAW", "A102", 10000, ""),
    ("DEPOSIT", "A101", 1000, ""),
    ("DEPOSIT", "A101", 1000, ""),
    ("TRANSFER", "A103", 500, "A101"),
    ("WITHDRAW", "A999", 500, ""),
    ("DEPOSIT", "A102", -200, "")
]

valid_transactions = []
invalid_transactions = []
transaction_patterns = {}
suspicious_patterns = []

print("----- INITIAL ACCOUNT BALANCES -----")
for account, balance in accounts.items():
    print(account, ":", balance)
for i, transaction in enumerate(transactions, start=1):
    operation, sender, amount, receiver = transaction
    error = ""

    if amount <= 0:
        error = "Invalid amount"
    elif sender not in accounts:
        error = "Account does not exist"
    elif operation == "WITHDRAW":
        if accounts[sender] < amount:
            error = "Insufficient balance"
        else:
            accounts[sender] -= amount

    elif operation == "DEPOSIT":
        accounts[sender] += amount

    elif operation == "TRANSFER":
        if receiver not in accounts:
            error = "Receiver account does not exist"
        elif accounts[sender] < amount:
            error = "Insufficient balance"
        else:
            accounts[sender] -= amount
            accounts[receiver] += amount

    else:
        error = "Invalid operation"

    if error:
        invalid_transactions.append((i, transaction, error))
        print("Transaction", i, "FAILED:", error)
    else:
        valid_transactions.append(transaction)
        print("Transaction", i, "SUCCESSFUL")

        # Detect repeated transaction patterns
        pattern = (operation, sender, amount, receiver)
        transaction_patterns[pattern] = (
            transaction_patterns.get(pattern, 0) + 1
        )
for pattern, count in transaction_patterns.items():
    if count >= 3:
        suspicious_patterns.append((pattern, count))

print("\n----- FINAL ACCOUNT BALANCES -----")
for account, balance in accounts.items():
    print(account, ":", balance)

print("\n----- TRANSACTION SUMMARY -----")
print("Total transactions:", len(transactions))
print("Successful transactions:", len(valid_transactions))
print("Invalid transactions:", len(invalid_transactions))

print("\n----- INVALID TRANSACTIONS -----")
if invalid_transactions:
    for number, transaction, reason in invalid_transactions:
        print("Transaction", number, ":", reason)
else:
    print("No invalid transactions")

print("\n----- SUSPICIOUS REPEATED PATTERNS -----")
if suspicious_patterns:
    for pattern, count in suspicious_patterns:
        print(pattern, "repeated", count, "times")
else:
    print("No suspicious repeated patterns detected")

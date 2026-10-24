def calculate_fare(base_fare, category):
    if category == "Adult":
        return base_fare
    elif category == "Child":
        return base_fare * 0.5
    elif category == "Senior":
        return base_fare * 0.7
    else:
        return base_fare
routes = {
    "Route A": 100,
    "Route B": 200,
    "Route C": 300
}

passenger_categories = ["Adult", "Child", "Senior"]

expected_revenue = 0
collected_revenue = 0

print("PASSENGER FARE AND REVENUE SYSTEM")
print("---------------------------------")

n = int(input("Enter number of passenger bookings: "))

for i in range(n):
    print("\nPassenger", i + 1)

    print("Available Routes:", list(routes.keys()))
    route = input("Enter route: ")

    if route not in routes:
        print("Invalid route! Booking skipped.")
        continue

    category = input(
        "Enter category (Adult/Child/Senior): "
    )

    if category not in passenger_categories:
        print("Invalid category! Booking skipped.")
        continue

    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        print("Invalid ticket quantity! Booking skipped.")
        continue

    base_fare = routes[route]
    fare = calculate_fare(base_fare, category)
    total_fare = fare * tickets

    expected_revenue += total_fare

    print("Route:", route)
    print("Passenger Category:", category)
    print("Fare per Ticket: Rs.", fare)
    print("Total Expected Fare: Rs.", total_fare)

    collected = float(
        input("Enter actual amount collected: Rs. ")
    )

    collected_revenue += collected
difference = collected_revenue - expected_revenue

print("\n========== REVENUE REPORT ==========")
print("Expected Revenue: Rs.", expected_revenue)
print("Collected Revenue: Rs.", collected_revenue)
print("Difference: Rs.", difference)

if difference == 0:
    print("Status: Revenue reconciled successfully.")
elif difference < 0:
    print("Status: Revenue shortage of Rs.", abs(difference))
else:
    print("Status: Excess collection of Rs.", difference)

print("====================================")

n = int(input("Enter number of products: "))

products = []

for i in range(n):
    print("\nEnter details for Product", i + 1)

    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    closing = int(input("Actual closing stock: "))
    minimum = int(input("Minimum required stock: "))
    expected = opening + incoming - dispatched
    discrepancy = closing - expected
    if closing < minimum:
        replenish = minimum - closing
    else:
        replenish = 0

    products.append([
        name, opening, incoming, dispatched,
        closing, expected, discrepancy, replenish
    ])
print("\n========== STOCK REPORT ==========")

for p in products:
    print("\nProduct:", p[0])
    print("Opening Stock:", p[1])
    print("Incoming Quantity:", p[2])
    print("Dispatched Quantity:", p[3])
    print("Actual Closing Stock:", p[4])
    print("Expected Closing Stock:", p[5])

    if p[6] == 0:
        print("Stock Status: No discrepancy")
    elif p[6] < 0:
        print("Stock Status: Stock shortage of", abs(p[6]))
    else:
        print("Stock Status: Extra stock of", p[6])

    print("Replenishment Required:", p[7])
total_replenishment = sum(p[7] for p in products)
total_discrepancies = sum(1 for p in products if p[6] != 0)

print("\n========== SUMMARY ==========")
print("Total Products:", n)
print("Products with Discrepancies:", total_discrepancies)
print("Total Replenishment Required:", total_replenishment)

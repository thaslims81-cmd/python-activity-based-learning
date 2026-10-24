raw_materials = {
    "Steel": 100,
    "Plastic": 200,
    "Copper": 50
}
material_required = {
    "Steel": 2,
    "Plastic": 3,
    "Copper": 1
}
planned_production = 40
order_demand = 45
defect_count = 5
defect_limit = 5

print("===== PRODUCTION ANALYSIS SYSTEM =====")

print("\n1. Raw Material Availability")
for material in raw_materials:
    required = planned_production * material_required[material]
    available = raw_materials[material]

    print("\nMaterial:", material)
    print("Available:", available)
    print("Required:", required)

    if available >= required:
        print("Status: Sufficient")
    else:
        shortage = required - available
        print("Status: Shortage of", shortage)
max_production = planned_production

for material in raw_materials:
    possible = raw_materials[material] // material_required[material]

    if possible < max_production:
        max_production = possible

print("\n2. Production Feasibility")
print("Planned Production:", planned_production)
print("Maximum Possible Production:", max_production)

if max_production >= planned_production:
    print("Status: Production is feasible")
else:
    print("Status: Production is not feasible")
print("\n3. Order Demand Analysis")
print("Customer Order Demand:", order_demand)

if max_production >= order_demand:
    print("Status: Order can be fulfilled")
else:
    print("Status: Order cannot be fulfilled")
    print("Production Shortage:", order_demand - max_production)
print("\n4. Quality Analysis")
print("Total Planned Production:", planned_production)
print("Defective Products:", defect_count)

defect_percentage = (defect_count / planned_production) * 100

print("Defect Percentage:", round(defect_percentage, 2), "%")
print("Maximum Allowed Defect Percentage:", defect_limit, "%")

if defect_percentage <= defect_limit:
    print("Quality Status: Acceptable")
else:
    print("Quality Status: Quality Violation Detected")
print("\n5. Final Summary")
print("Planned Production:", planned_production)
print("Maximum Possible Production:", max_production)
print("Order Demand:", order_demand)
print("Defects:", defect_count)
print("Defect Rate:", round(defect_percentage, 2), "%")

if max_production >= order_demand and defect_percentage <= defect_limit:
    print("Overall Status: Production and Quality Targets Met")
else:
    print("Overall Status: Action Required")

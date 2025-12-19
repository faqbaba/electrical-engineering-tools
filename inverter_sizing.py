print("INVERTER SIZING TOOL 🔋")
print("----------------------")

appliances = []
total_load = 0

while True:
    name = input("Enter appliance name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    while True:
        try:
            power = float(input(f"Enter power rating of {name} (W): "))
            break
        except ValueError:
            print("Please enter a valid number!")

    appliances.append((name, power))
    total_load += power

print("\nAppliance List:")
for item in appliances:
    print(f"- {item[0]}: {item[1]} W")

print(f"\nTotal Load = {total_load} W")

# Inverter sizing
inverter_va = total_load * 1.3
print(f"Recommended Inverter Size ≈ {inverter_va:.0f} VA")

# Battery sizing
while True:
    try:
        backup_hours = float(input("\nEnter desired backup time (hours): "))
        break
    except ValueError:
        print("Please enter a valid number!")

battery_voltage = 12
battery_ah = (total_load * backup_hours) / battery_voltage

print(f"Estimated Battery Capacity ≈ {battery_ah:.0f} Ah (12V)")

print("\nSizing completed ✅")

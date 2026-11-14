battery_percentage = int(input("Enter battery percentage: "))
wind_speed = int(input("Enter wind speed (km/h): "))
package_weight = float(input("Enter package weight (kg): "))

print("\n--- Decision Engine Activated ---")

if battery_percentage < 20:
    print("ACTION: Low Power. Returning to Charging Station.")

elif wind_speed >= 45:
    print("ACTION: High Winds Detected. Aborting Mission for Safety.")

elif 15 <= package_weight <= 25:
    print("ACTION: Heavy Package Detected. Activating Dual-Engine Mode.")

elif package_weight >25:
    print("ACTION: Overweight Limit. Please reduce load to proceed.")

elif battery_percentage > 20 and wind_speed < 45 and package_weight < 15:
    print("ACTION: All Systems Nominal. Mission Start!")

else:
    print("ACTION: Conditions unclear. Manual inspection required.")
print("\n--- Decision Engine Activated ---")

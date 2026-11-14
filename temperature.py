temperature = float(input("Enter the current house temperature (°C): "))

if temperature > 28:
    print("It is too hot. Turning on the AC.")

elif temperature < 18:
    print("It is too cold. Turning on the heater.")

else:
    print("The temperature is perfect. No action needed.")

print("Smart system check complete.")

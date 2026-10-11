def pump_on():
    print("Pump running...")

water_heater = int(input("How many gallons are in a water heater tank? "))
passes = 0
while water_heater > 0:
    pump_on()
    if water_heater >= 7:
        water_heater -= 7
    else:
        water_heater = 0
    passes += 1
    print(f"There are {water_heater} gallons of water left.")
print(f"It took {passes} passes to drain the water heater.")

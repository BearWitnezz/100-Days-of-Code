# TODO 1: Define pump_on() with a docstring. It prints "Pump running...".

# TODO 2: Ask "How many gallons are in a water heater tank?" and save the answer as an int.

# TODO 3: Start a pass counter at 0.

# TODO 4: Loop while any gallons are left. Call pump_on() on every pass.

# TODO 5: If at least 7 gallons are left, subtract 7. Otherwise set the gallons to 0.

# TODO 6: Add 1 to the pass counter, then print how many gallons are left.

# TODO 7: After the tank is empty, print how many passes it took to drain the water heater.

def pump_on():
    """Announce that the pump is running."""
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

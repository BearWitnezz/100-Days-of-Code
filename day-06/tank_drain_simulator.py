# TODO 1: Define pump_on so each pass can announce that the pump is running.
# TODO 2: Ask how many gallons are in the tank.
# TODO 3: Remove up to 7 gallons on each pass until the tank is empty.
# TODO 4: Print the gallons left after each pass and how many passes it took.

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

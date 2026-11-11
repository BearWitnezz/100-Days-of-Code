# TODO 1: Print "Welcome to the tip calculator!".

# TODO 2: Ask "What was the total bill? $" and save the answer as a float.

# TODO 3: Ask "How much tip would you like to give? 10, 12, or 15?". Turn that percent into a multiplier:
#   percent / 100 + 1.

# TODO 4: Ask "How many people to split the bill?" and save the answer as an int.

# TODO 5: Each person's share is (bill / people) times that multiplier. Round it to 2 decimal places.

# TODO 6: Print "Each person should pay: $" and the rounded share.

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
each_tip = int(tip) / 100 + 1
people = int(input("How many people to split the bill? "))
each_person = round((total / people) * each_tip, 2)
print(f"Each person should pay: ${each_person}")

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
each_tip = int(tip) / 100 + 1
people = int(input("How many people to split the bill? "))
each_person = round((total / people) * each_tip, 2)
print(f"Each person should pay: ${each_person}")

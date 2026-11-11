# TODO 1: Print "Welcome to the Job Split Calculator".

# TODO 2: Ask for the job total as a float. Put a $ on its own line before the answer.

# TODO 3: Ask for the tax percentage as a float.

# TODO 4: Ask how many people are splitting the total, and save that as an int.

# TODO 5: Each person's share is (job total / number of people) times (tax percent / 100 + 1).

# TODO 6: Print "Each person pays $" and the share, with two digits after the decimal.

print("Welcome to the Job Split Calculator")
job_total = float(input("What was the total amount for the job?\n$"))
tax_percent = float(input("What was the tax percentage for the job?\n"))
number_of_people = int(input("How many people are splitting the total?\n"))
each_person_pays = (job_total / number_of_people) * (tax_percent / 100 + 1)
print(f"Each person pays ${each_person_pays:.2f}")

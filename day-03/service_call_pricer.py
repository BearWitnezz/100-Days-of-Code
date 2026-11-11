# TODO 1: Start the bill at 0. Print "Welcome to the Service Call Pricer!".

# TODO 2: Ask which job this is: d for drain, w for water heater, or l for leak. Compare the answer in lowercase.

# TODO 3: Add 150 for a drain, 1200 for a water heater, or 250 for a leak. Any other letter prints "Unknown job"
#   and leaves the bill at 0.

# TODO 4: Ask "Is it an emergency? (y/n)". Add 100 when the answer is y.

# TODO 5: Ask for the customer's age as a whole number. At 65 or older, take 10 percent off the bill so far.

# TODO 6: Ask "Is it the weekend? (y/n)" and "Is it after 6pm? (y/n)". If either answer is y, add 75.

# TODO 7: Print "Your total bill is $" with the bill shown to two decimal places.

bill = 0
print("Welcome to the Service Call Pricer!")
job_type = input("What is the type of job being performed? "
                 "Select d for drain, w for water heater, or l for leak. ").lower()
if job_type == "d":
    bill += 150
elif job_type == "w":
    bill += 1200
elif job_type == "l":
    bill += 250
else:
    print("Unknown job")
emergency = input("Is it an emergency? (y/n) ").lower()
if emergency == "y":
    bill += 100
customers_age = int(input("What is your age? "))
if customers_age >= 65:
    bill = bill - (bill * 0.1)
weekend = input("Is it the weekend? (y/n) ").lower()
after_6pm = input("Is it after 6pm? (y/n) ").lower()
if weekend == "y" or after_6pm == "y":
    bill += 75
print(f"Your total bill is ${bill:.2f}")

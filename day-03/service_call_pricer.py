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

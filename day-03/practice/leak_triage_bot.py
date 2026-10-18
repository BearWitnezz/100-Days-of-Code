print("Welcome to the Leak Triage Bot")
water_spraying = input("Is water spraying?\n").lower()
near_electrical = input("Is it near an electrical unit?\n").lower()
if water_spraying == "yes" or near_electrical == "yes":
    print("Ok this is an emergency!")
    house_shutoff = input("Is there a working house shutoff?\n").lower()
    if house_shutoff == "yes":
        print("Ok on my way!")
    else:
        print("Contact the city first to have your water shutoff.")
else:
    print("This is not an emergency.")

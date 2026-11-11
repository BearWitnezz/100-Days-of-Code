# TODO 1: Print "Welcome to the Leak Triage Bot".

# TODO 2: Ask "Is water spraying?" and "Is it near an electrical unit?". Save both answers in lowercase.

# TODO 3: If either answer is "yes", print "Ok this is an emergency!" and ask "Is there a working house shutoff?".
#   Save that answer in lowercase too.

# TODO 4: When the shutoff answer is "yes", print "Ok on my way!".

# TODO 5: When the shutoff answer is anything else, print "Contact the city first to have your water shutoff."

# TODO 6: If water is not spraying and it is not near electrical equipment, print "This is not an emergency."

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

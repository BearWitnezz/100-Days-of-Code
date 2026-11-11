# TODO 1: Welcome the user to the van name generator.
# TODO 2: Ask for a favorite tool and the street they grew up on.
# TODO 3: Join the two answers into a van name and print it.

print("Welcome to the Van Name Generator")
favorite_tool = input("What is your favorite tool?\n")
street = input("What street did you grow up on?\n")
van_name = (favorite_tool + " " + street)
print(f"Your van name is {van_name}")

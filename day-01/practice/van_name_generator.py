# TODO 1: Print "Welcome to the Van Name Generator".

# TODO 2: Ask "What is your favorite tool?" and save the answer.

# TODO 3: Ask "What street did you grow up on?" and save that answer too.

# TODO 4: Join the tool and the street with one space between them, and save that string as the van name.

# TODO 5: Print the van name in a sentence: "Your van name is {van name}".
#   Nudge: an f-string can drop the saved name into that sentence.

print("Welcome to the Van Name Generator")
favorite_tool = input("What is your favorite tool?\n")
street = input("What street did you grow up on?\n")
van_name = (favorite_tool + " " + street)
print(f"Your van name is {van_name}")

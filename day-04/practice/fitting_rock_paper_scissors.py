# Wrench beats pipe, pipe beats plunger, and plunger beats wrench.
import random
fittings = ["wrench","pipe","plunger"]
computer_choice = random.choice(fittings)
print("Welcome to the fittings version of Rock Paper Scissors")
user_choice = input("Choose: wrench, pipe, or plunger.\n").lower()
if user_choice not in fittings:
    print("Not a valid choice!")
else:
    print(f"Computer chose: {computer_choice}")
    if computer_choice == user_choice:
        print("Tie!")
    elif computer_choice == "wrench" and user_choice == "plunger":
        print("You win!")
    elif computer_choice == "pipe" and user_choice == "wrench":
        print("You win!")
    elif computer_choice == "plunger" and user_choice == "pipe":
        print("You win!")
    else:
        print("You lose!")

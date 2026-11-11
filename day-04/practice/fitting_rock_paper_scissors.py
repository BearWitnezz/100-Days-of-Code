# TODO 1: Import random. The three fittings are wrench, pipe, and plunger.
#   Wrench beats pipe, pipe beats plunger, and plunger beats wrench.

# TODO 2: Let the computer pick one fitting at random.

# TODO 3: Print "Welcome to the fittings version of Rock Paper Scissors".

# TODO 4: Ask "Choose: wrench, pipe, or plunger." and save the answer in lowercase.

# TODO 5: If that answer is not one of the three fittings, print "Not a valid choice!" and skip the match.

# TODO 6: Otherwise print "Computer chose: " and the computer's fitting.

# TODO 7: The same choice on both sides prints "Tie!".

# TODO 8: The player wins when the computer has wrench and the player has plunger, the computer has pipe and the
#   player has wrench, or the computer has plunger and the player has pipe. Print "You win!".

# TODO 9: Every other matchup prints "You lose!".

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

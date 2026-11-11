# TODO 1: Print "Welcome to Treasure Island." and "Your mission is to find the treasure."

# TODO 2: Ask "Left or Right?" and save the answer in lowercase.

# TODO 3: "right" prints "Fall into a hole. Game Over!". Any first answer other than "left" or "right" prints
#   "Sorry, that's not a valid answer. Game Over!".

# TODO 4: Only "left" continues. Ask "Swim or Wait?" and lowercase that answer too.

# TODO 5: "swim" prints "Attacked by trout. Game Over!". Anything other than "swim" or "wait" prints
#   "Sorry, that's not a valid answer. Game Over!".

# TODO 6: Only "wait" continues. Ask "Which door? Yellow, Blue, or Red." and lowercase the answer.

# TODO 7: "blue" prints "Eaten by beasts. Game Over!". "red" prints "Burned by fire. Game Over!".
#   "yellow" prints "Congratulations, you win!". Any other door prints "Sorry, that's not a valid door. Game Over!".

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("Left or Right? ").lower()
if choice_1 == "left":
    choice_2 = input("Swim or Wait? ").lower()
    if choice_2 == "wait":
        choice_3 = input("Which door? Yellow, Blue, or Red. ").lower()
        if choice_3 == "blue":
            print("Eaten by beasts. Game Over!")
        elif choice_3 == "red":
            print("Burned by fire. Game Over!")
        elif choice_3 == "yellow":
            print("Congratulations, you win!")
        else:
            print("Sorry, that's not a valid door. Game Over!")
    elif choice_2 == "swim":
        print("Attacked by trout. Game Over!")
    else:
        print("Sorry, that's not a valid answer. Game Over!")
elif choice_1 == "right":
    print("Fall into a hole. Game Over!")
else:
    print("Sorry, that's not a valid answer. Game Over!")

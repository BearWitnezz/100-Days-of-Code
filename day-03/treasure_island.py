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

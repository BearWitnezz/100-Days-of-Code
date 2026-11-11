# TODO 1: Import random.

# TODO 2: Store the ASCII art for rock, paper, and scissors in three strings. Put those strings in a list in that
#   order, so 0 is rock, 1 is paper, and 2 is scissors.

# TODO 3: Ask "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors". Keep the answer as text.

# TODO 4: Print the rock art for "0", the paper art for "1", and the scissors art for "2".

# TODO 5: Only when the answer is "0", "1", or "2", let the computer pick one of the three pictures at random and
#   print "Computer chose:" plus that picture.

# TODO 6: Rock ties rock, loses to paper, and beats scissors. Paper beats rock, ties paper, and loses to scissors.
#   Scissors loses to rock, beats paper, and ties scissors. Print "It's a tie!", "You lose!", or "You win!".
#   Nudge: the player's answer is the text "0", "1", or "2". The computer's choice is the art string itself.

# TODO 7: Any other input prints "Invalid input" and does not play a round.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

player = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n")
if player == "0":
    print(rock)
elif player == "1":
    print(paper)
elif player == "2":
    print(scissors)

if player == "0" or player == "1" or player == "2":

    computer_choice = random.choice(choices)
    print("Computer chose:" + computer_choice)

    if player == "0" and computer_choice == rock:
        print("It's a tie!")
    elif player == "0" and computer_choice == paper:
        print("You lose!")
    elif player == "0" and computer_choice == scissors:
        print("You win!")
    elif player == "1" and computer_choice == rock:
        print("You win!")
    elif player == "1" and computer_choice == paper:
        print("It's a tie!")
    elif player == "1" and computer_choice == scissors:
        print("You lose!")
    elif player == "2" and computer_choice == rock:
        print("You lose!")
    elif player == "2" and computer_choice == paper:
        print("You win!")
    elif player == "2" and computer_choice == scissors:
        print("It's a tie!")

else:
    print("Invalid input")

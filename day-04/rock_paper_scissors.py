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

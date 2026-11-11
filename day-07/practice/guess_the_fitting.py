# TODO 1: Import random. The fittings are elbow, coupling, flange, and valve.

# TODO 2: Pick one fitting at random. Start with 6 lives, and start game_over as False.

# TODO 3: Build a display list with one "_" for each letter, and print it.

# TODO 4: Loop while the game is not over. Ask "Enter your guess: " and lowercase it.

# TODO 5: Walk the fitting by position. Wherever the guess matches that letter, put the letter into the display.

# TODO 6: If the guess is not in the fitting at all, lose one life and print "Wrong guess. Lives: " plus the lives
#   that are left.

# TODO 7: Print the display after every guess.

# TODO 8: At 0 lives, print "Game Over. You lost!" and set game_over to True.

# TODO 9: If the display has no "_" left, print "You win!" and set game_over to True.

import random
plumbing_words = ["elbow","coupling","flange","valve"]
computer_choice = random.choice(plumbing_words)
display = []
lives = 6
game_over = False
for letter in computer_choice:
    display.append("_")
print(display)
while not game_over:
    guess = input("Enter your guess: ").lower()
    for position in range(len(computer_choice)):
        if guess == computer_choice[position]:
            display[position] = guess
    if guess not in computer_choice:
        lives -= 1
        print(f"Wrong guess. Lives: {lives}")
    print(display)
    if lives == 0:
        print("Game Over. You lost!")
        game_over = True
    if "_" not in display:
        print("You win!")
        game_over = True

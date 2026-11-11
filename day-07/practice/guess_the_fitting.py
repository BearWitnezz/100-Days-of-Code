# TODO 1: Pick a plumbing fitting and show a blank for each letter.
# TODO 2: Ask for letters until the word is complete or the lives hit zero.
# TODO 3: Fill the letter in wherever it appears, and lose a life on a miss.
# TODO 4: Print whether the player won or lost.

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

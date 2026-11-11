# TODO 1: Import Turtle and Screen from turtle, and import random. Start the race as not running.

# TODO 2: Make a screen that is 500 wide and 400 tall.

# TODO 3: Pop up a text box titled "Make your bet" that asks "Which turtle will win the race? Enter a color: ".
#   Print whatever the user typed.

# TODO 4: The colors are red, orange, yellow, green, blue, and violet. Start an empty list to hold the turtles.

# TODO 5: The starting line is x = -230. The first turtle's y is -100, and each next turtle sits 50 higher.

# TODO 6: For each color, make a turtle with the "turtle" shape, set its color, lift the pen, send it to its
#   starting x and y, then append it to the list.

# TODO 7: If the user actually typed a bet, start the race.

# TODO 8: While the race is on, every turtle moves forward by a random distance from 0 to 10.

# TODO 9: The first turtle whose x coordinate is past 230 wins. Stop the race and read that turtle's pen color.
#   Nudge: leave the turtle loop as soon as one turtle wins, so a later turtle on the same pass cannot also win.

# TODO 10: If that color is the bet, print "You won! The {color} turtle is the winner!". Otherwise print
#   "You lost! The {color} turtle is the winner!".

# TODO 11: Close the window when it is clicked.

from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
x_position = -230
y_position = -100

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x_position,y_position)
    y_position += 50
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
            break
screen.exitonclick()

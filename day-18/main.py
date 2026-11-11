# TODO 1: The spot colors come from the Hirst painting. colorgram.extract can pull them out of the image: for each
#   extracted color, save (red, green, blue) in a list. Keep that finished list of RGB tuples in the program.
#   This file's list is those colors, starting with (133, 164, 202).

# TODO 2: Import random, and import turtle, Turtle, and Screen.

# TODO 3: Define hirst(rows) with a docstring. Set the turtle color mode to 255 so a dot can take an RGB tuple.

# TODO 4: Make one turtle, set its shape to "turtle", and lift the pen so the move between dots does not draw a line.

# TODO 5: Start the turtle at x = -255 and y = -255.

# TODO 6: For each row, paint 10 dots. Each dot is 20 pixels wide and uses a random color from the list. After a
#   dot, move forward 50.

# TODO 7: After a row, add 50 to y and teleport back to x = -255 at that new y.

# TODO 8: Hide the turtle when the rows are done.

# TODO 9: Call hirst with 10 rows.

# TODO 10: Make a screen and close the window when it is clicked.

# import colorgram
# colors = colorgram.extract('hirst.jpg', 24)
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list_of_colors.append((r,g,b))
# print(list_of_colors)

color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88),
                  (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99),
                  (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55),
                  (15, 96, 71), (33, 60, 106)]
import random
import turtle
from turtle import Turtle, Screen


def hirst(rows):
    """Paint a Hirst-style spot painting with the given number of rows."""
    turtle.colormode(255)
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    y = -255
    tim.teleport(-255, y)
    for _ in range(rows):
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
        y += 50
        tim.teleport(-255, y)
    tim.ht()


hirst(10)

screen = Screen()
screen.exitonclick()

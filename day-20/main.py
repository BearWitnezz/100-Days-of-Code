# TODO 1: Set up the screen: 600x600, black background, title "My Snake Game", exitonclick at the bottom.

# TODO 2: Make 3 white square segments in a row with no gaps. (Each turtle is 20 pixels wide.)

# TODO 3: Redo TODO 2 with a loop over a list of starting positions.

# TODO 4: Lift the pen so the segments don't draw lines, and turn off the animation (tracer) so the screen only
#  refreshes when you call update.

# TODO 5: Make the snake move by itself in a while loop, with a short sleep each pass. (Nudge: move the tail to where
#  the segment ahead of it was, working back to front, then move the head.)

# TODO 6: Make a new snake.py with a Snake class. When you create one, it builds the 3-segment snake on its own.
#   Nudge: anything the class owns needs self. in front of it.

# TODO 7: Give Snake a move() method that does the old tail-follows-head loop.

# TODO 8: Pull STARTING_POSITIONS and MOVE_DISTANCE out as ALL_CAPS constants at the top of snake.py.

# TODO 9: Trim main.py down to screen setup, snake = Snake(), and the game loop calling snake.move().

# TODO 10: In main.py, after you create the snake, listen for keystrokes and bind the arrow keys to snake.up, snake.down, snake.left, and snake.right.
#   Nudge: the key names are "Up", "Down", "Left", and "Right". Remember how you pass a method to onkey.

# TODO 11: Add up, down, left, and right methods on Snake that turn the head with setheading.
#   Nudge: the head is the first item in your list. Headings go counterclockwise from 0 (east).

# TODO 12: Save the head as its own attribute after the snake is built, then use it in move() and the direction methods.

# TODO 13: Add UP, DOWN, LEFT, and RIGHT constants, and don't let the snake reverse into itself.
#   Nudge: only change heading if it's not already going the opposite way, and heading is a method.

from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

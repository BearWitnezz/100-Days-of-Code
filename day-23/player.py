# TODO 1: Player already inherits from Turtle. In __init__, run the parent initializer first with super().__init__().

# TODO 2: Make it look like a turtle, lift the pen, point it north, and send it to STARTING_POSITION.
#   Nudge: a turtle shape starts facing east, so you have to set the heading. Use the constant, not a typed-in number.

# TODO 3: Fill in go_up() so it moves the player forward by MOVE_DISTANCE.

# TODO 4: Fill in go_to_start() so it sends the player back to STARTING_POSITION.

# TODO 5: Fill in is_at_finish_line() so it returns True or False for "has the player's y gone past FINISH_LINE_Y?"
#  — return the comparison itself.

from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Builds the player turtle at the starting position, facing north."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def go_up(self):
        """Moves the player forward by the move distance."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Sends the player back to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Returns True if the player has reached the finish line."""
        return self.ycor() > FINISH_LINE_Y

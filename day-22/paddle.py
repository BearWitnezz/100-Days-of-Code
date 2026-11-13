# TODO 1: Create a Paddle class that inherits from Turtle, and run the parent's initializer first with super().__init__().

# TODO 2: Have __init__ take a position (a tuple like (350, 0)). Make the paddle a white square stretched to 20 wide by 100 tall, pen up, then send it to that position.
#   Nudge: every turtle starts 20x20. stretch_wid is up-and-down and stretch_len is side-to-side. Inside the class use self., not a second Turtle.

# TODO 3: Add a go_up() method that moves the paddle 20 pixels up. Only y changes; keep the paddle's current x.
#   Nudge: save the new y first (self.ycor() + 20), then goto it.

# TODO 4: Add a go_down() method that does the same thing but 20 pixels down. Give every method a one-sentence docstring.

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        """Builds a white 20x100 paddle at the given position."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddle up."""
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def go_down(self):
        """Moves the paddle down."""
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)

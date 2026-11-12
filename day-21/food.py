# TODO 1: Create a Food class that inherits from Turtle. In __init__, run the Turtle initializer so Food gets everything a turtle can do.
#   Nudge: same two steps as the Fish example — the parent class in parentheses after the name, and super().__init__().

# TODO 2: In __init__, make the food a small circle that doesn't draw a trail: circular shape, pen up, shrink it to 10x10 (default is 20x20, stretch length and width by 0.5), set a color (lesson used blue), and set speed to "fastest" so you don't see it animate from the center.

# TODO 3: Place the food at a random spot, not right at the edge. The screen is 600x600 (axes go to 300). The lesson used random.randint(-280, 280) for both x and y, then goto that point.

# TODO 4: Pull the random move into a refresh() method and call self.refresh() from __init__. Give every function a one-sentence docstring.

from turtle import Turtle
import random

class Food(Turtle):
    """Set up the food object."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food object to a random position."""
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

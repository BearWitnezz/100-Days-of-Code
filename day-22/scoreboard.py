# TODO 1: Create a Scoreboard class that inherits from Turtle. Make it white, pen up, and hidden (it only writes).

# TODO 2: Give it a left score and a right score, both starting at 0.

# TODO 3: Add update_scoreboard(): clear the old text, then write the left score at (-100, 200) and the right score at (100, 200), centered, in Courier 80 normal. Call it once from __init__.
#   Nudge: don't name it update, because Turtle already has an update() method. Without clear() the new score writes on top of the old one.

# TODO 4: Add l_point() and r_point(): add 1 to that side's score, then update the scoreboard. Give every method a one-sentence docstring.

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        """Sets up a hidden white writer with both scores at 0."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Add 1 point to the left side."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Add 1 point to the right side."""
        self.r_score += 1
        self.update_scoreboard()

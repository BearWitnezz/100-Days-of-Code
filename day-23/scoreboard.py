# TODO 1: Scoreboard already inherits from Turtle. In __init__, run the parent initializer, hide the turtle, lift the
#  pen, and start the level at 1.

# TODO 2: Park it near the top left, then write the starting level using FONT.

# TODO 3: Fill in update_scoreboard() so it clears the old text and writes "Level: " plus the current level. Call it
#  once from __init__ after setup.
#   Nudge: don't name it update, because Turtle already has an update() method. Without clear(), the new level writes
#   on top of the old one.

# TODO 4: Fill in increase_level() so it adds 1 to the level, then refreshes the scoreboard.

# TODO 5: Fill in game_over() so it goes to the center and writes GAME OVER with the same font. Don't clear first, so
#  the level stays visible.

from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Sets up a hidden writer and shows the starting level."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the old text and writes the current level."""
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)


    def increase_level(self):
        """Adds one to the level and refreshes the display."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Writes GAME OVER in the center of the screen."""
        self.home()
        self.write("GAME OVER",align="center",font=FONT)

# TODO 1: Create a Scoreboard class that inherits from Turtle. In __init__, run the Turtle initializer and start self.score at 0.

# TODO 2: Set up the turtle before you write: color it white (black screen), hide it, lift the pen, and move to the top center (lesson used (0, 270)). If this happens after write, you'll get an invisible score in the middle with a line behind it.

# TODO 3: Write the starting score so it reads "Score: 0". The font argument is a tuple of (name, size, style), not a single string. Pick whatever font and size you like.

# TODO 4: Pull ALIGNMENT and FONT out as constants at the top of the file and use them in write().

# TODO 5: Add an update() method that only writes the current score. Call it from __init__ after setup so "Score: 0" appears at the start.

# TODO 6: Add increase_score() that adds 1 to the object's score, clears the old text, then calls update().
#   Nudge: clear goes in increase_score, not in update, so __init__ doesn't clear on the first write. Use self.score += 1 — __init__ already set it to 0 once.

# TODO 7: Add game_over() that goes to (0, 0) and writes "GAME OVER" with the same alignment and font. Do not clear first, so the final score stays visible at the top. One-sentence docstring on every function.

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Set up the scoreboard and write the starting score."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0,y=270)
        self.update()

    def update(self):
        """Write the new score on the screen."""
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Add one to the score and refresh the display."""
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        """Write the game over on the screen."""
        self.setposition(x=0,y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

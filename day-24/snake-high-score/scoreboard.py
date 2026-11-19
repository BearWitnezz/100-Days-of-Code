# TODO 1: Create a Scoreboard class that inherits from Turtle. In __init__, run the Turtle initializer and start
#  self.score at 0.

# TODO 2: Set up the turtle before you write: color it white (black screen), hide it, lift the pen, and move to the top
#  center (lesson used (0, 270)). If this happens after write, you'll get an invisible score in the middle with a line
#  behind it.

# TODO 3: Write the starting score so it reads "Score: 0". The font argument is a tuple of (name, size, style), not a
#  single string. Pick whatever font and size you like.

# TODO 4: Pull ALIGNMENT and FONT out as constants at the top of the file and use them in write().

# TODO 5: Add an update() method that writes the current score and the high score. Call it from __init__ after setup
#  so the starting scores appear at the start.

# TODO 6: Add increase_score() that adds 1 to the object's score and then calls update(). Move self.clear() into
#  update() so it runs on every refresh.
#   Nudge: you couldn't clear inside update before, because game over needed the score to stay on screen. Use
#   self.score += 1 — __init__ already set it to 0 once.

# TODO 7: Replace game_over() with reset(): if self.score is greater than self.high_score, update the high score first,
#  then set self.score to 0, then call update().
#   Nudge: order matters. If you set the score to 0 first, it can never beat the high score.

# TODO 8: In __init__, swap out high_score = 0. Open data.txt (with with), read it, and save it on self as the
#  high score. What type does read() give back, and what type do you need?

# TODO 9: In reset(), right after you set a new high score, open data.txt again so you can write to it. Which mode?

# TODO 10: Write the high score into the file. What type does write() need?

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Set up the scoreboard and write the starting score."""
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0,y=270)
        self.update()

    def update(self):
        """Write the new score on the screen."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Add one to the score and refresh the display."""
        self.score += 1
        self.update()

    def reset(self):
        """If the score beats the high score, save it, then set the score back to 0 and refresh the display."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     """Write the game over on the screen."""
    #     self.setposition(x=0,y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

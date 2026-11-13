# TODO 1: Create a Ball class that inherits from Turtle. Make it a white circle, pen up, starting at the center.

# TODO 2: Give the ball attributes for how far it moves each step on x and on y (both start at 10), plus a move_speed that starts at 0.1.
#   Nudge: don't name it speed, because Turtle already has a speed() method.

# TODO 3: Add a move() method that moves the ball by its current x and y step from where it is now.

# TODO 4: Add bounce_y() that flips the y direction.
#   Nudge: multiply the current value by -1 so it flips every time, not just once.

# TODO 5: Add bounce_x() that flips the x direction and makes the ball a little faster (shrink move_speed by multiplying it by a number a bit less than 1, like 0.9).

# TODO 6: Add reset_position() that sends the ball back to the center, serves it toward the other player, and puts move_speed back to 0.1. Give every method a one-sentence docstring.

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """Builds a white ball at the center with its starting step and speed."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.home()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball by its current x and y step."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Flips the y direction."""
        self.y_move *= -1

    def bounce_x(self):
        """Flips the x direction and speeds the ball up."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the position of the ball to the center and serves the other player."""
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

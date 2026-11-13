# TODO 1: Set up the screen: 800 wide by 600 tall, black background, title "Pong", and exitonclick at the bottom.

# TODO 2: Turn the animation off with tracer(0) right after the screen setup, before any paddles or ball are made, so nothing slides in from the center.
#   Nudge: once animation is off, the screen only redraws when you call screen.update().

# TODO 3: Create a right paddle at (350, 0) and a left paddle at (-350, 0) from the Paddle class.
#   Nudge: you make an object by calling the class, passing the position tuple in.

# TODO 4: Create a Ball and a Scoreboard. Import each class from its own file.

# TODO 5: Listen for keys. Bind "Up"/"Down" to the right paddle's go_up/go_down and "w"/"s" to the left paddle's.
#   Nudge: pass the methods without parentheses.

# TODO 6: Run a game loop while game_is_on: update the screen, move the ball, and sleep by the ball's move_speed.

# TODO 7: Detect collision with the top and bottom walls. If the ball's y goes past 280 or below -280, bounce it on y.

# TODO 8: Detect collision with either paddle. The ball is within 50 of the right paddle and its x is past 320, OR within 50 of the left paddle and its x is below -320. Then bounce it on x.
#   Nudge: distance() measures center to center, so a hit near the paddle's end looks far away. That's why you also need the x check.

# TODO 9: Detect when the right paddle misses (the ball's x goes past 400). Reset the ball and give the left player a point.

# TODO 10: Detect when the left paddle misses (the ball's x goes below -400). Reset the ball and give the right player a point.
#   Nudge: use a separate if for each side, since a different player scores.

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect ball going past right paddle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
    # Detect ball going past left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

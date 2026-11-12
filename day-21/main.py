# TODO 1: Set up the screen: 600x600, black background, title "My Snake Game", tracer(0) so it only refreshes when you call update, and exitonclick at the bottom.

# TODO 2: Create a Snake, a Food, and a Scoreboard. Import each class from its own file.

# TODO 3: Listen for keystrokes and bind the arrow keys to snake.up, snake.down, snake.left, and snake.right.
#   Nudge: the key names are "Up", "Down", "Left", and "Right". Pass the methods without parentheses.

# TODO 4: Run a game loop while game_is_on: update the screen, sleep briefly, and call snake.move().

# TODO 5: After the snake moves, detect collision with food. If the head's distance to the food is less than 15, call food.refresh(), snake.extend(), and scoreboard.increase_score().
#   Nudge: don't also call scoreboard.update() — increase_score already does that.

# TODO 6: Detect collision with the wall. If the head's x or y has gone past 280 on any of the four sides, set game_is_on to False and call scoreboard.game_over().
#   Nudge: the screen goes to 300; 280 is the tested boundary.

# TODO 7: Detect collision with the tail. Loop through the snake's segments; if the head's distance to a segment is less than 10, set game_is_on to False and call scoreboard.game_over().
#   Nudge: skip the head (the first segment), or you'll get instant game over because the head's distance to itself is 0.

# TODO 8: Replace the "skip the head" if/pass with a slice: loop from the second segment to the end (omit the end number), then use a single if for the distance check.

from turtle import Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

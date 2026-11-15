# TODO 1: The screen is already 600 wide by 600 tall, with tracer off and a loop that sleeps 0.1 then updates.
#  Keep exitonclick at the bottom so the window stays open.

# TODO 2: Create a Player, a CarManager, and a Scoreboard. The imports from each file are already in place.

# TODO 3: Listen for keys and bind "Up" to the player's go_up method.
#   Nudge: pass the method without parentheses.

# TODO 4: In the loop, after the screen updates, tell the car manager to maybe create a car and to move all the cars.

# TODO 5: Detect a collision with a car. Loop through the cars; if the player is within 20 of one, turn the game off
#  and show GAME OVER.

# TODO 6: Detect a finished crossing. If the player has reached the finish line, send the player back to the start and
#  speed the cars up.

# TODO 7: When a crossing is finished, also increase the level on the scoreboard.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    # Detect collision with a car.
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect a finished crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()

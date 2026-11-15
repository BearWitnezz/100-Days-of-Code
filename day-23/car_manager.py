# TODO 1: CarManager does not inherit from Turtle. In __init__, give it a list to hold the cars and a current speed that
#  starts at STARTING_MOVE_DISTANCE.

# TODO 2: Fill in create_car(). Only about 1 in 6 calls should actually make a car, or the road fills up in one second.
#   Nudge: pick a random number and only build a car when you get one particular value. Import what you need at the top.

# TODO 3: Each new car is a square turtle stretched to 20 tall by 40 wide, a random color from COLORS, pen up, starting
#  at the right edge with a random y. Leave about 50 pixels clear at the top and bottom so cars don't spawn on the start
#  or finish. Append the car to the list.
#   Nudge: a turtle starts 20 by 20. stretch_wid is up-and-down and stretch_len is side-to-side.

# TODO 4: Fill in move_cars() so every car in the list moves left by the current speed.

# TODO 5: Fill in level_up() so the current speed increases by MOVE_INCREMENT.

from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """Sets up an empty car list and the starting movement speed."""
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        """Sometimes creates a new car at the right edge and adds it to the list."""
        if random.randint(1,6) == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300,random.randint(-250,250))
            new_car.setheading(180)
            self.cars.append(new_car)


    def move_cars(self):
        """Moves every car in the list to the left by the current speed."""
        for car in self.cars:
            car.forward(self.car_speed)


    def level_up(self):
        """Increases the cars' movement speed for the next level."""
        self.car_speed += MOVE_INCREMENT

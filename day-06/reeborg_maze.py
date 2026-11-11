# TODO 1: Add turn_right. This file runs in Reeborg's World, which has no turn_right.
# TODO 2: Add a helper that turns right and takes one step.
# TODO 3: Before the maze loop, put a wall on Reeborg's right so an open start cannot spin forever.
# TODO 4: Follow that right-hand wall until Reeborg reaches the goal.

def turn_right():
    """Turn Reeborg to the right."""
    turn_left()
    turn_left()
    turn_left()

def change_direction():
    """Turn right and take one step."""
    turn_right()
    move()

while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        change_direction()
    elif wall_in_front():
        turn_left()
    else:
        move()

# TODO 1: This version runs in Reeborg's World. Define turn_right() with a docstring. A right turn is three
#   left turns. turn_left and move already exist there.

# TODO 2: Define change_direction() with a docstring. It turns right, then takes one step.

# TODO 3: Loop until Reeborg is at the goal.

# TODO 4: If the front is clear and the right is clear, call change_direction().

# TODO 5: If there is a wall on the right and a wall in front, turn left.

# TODO 6: If there is a wall in front and the right is clear, call change_direction().

# TODO 7: Otherwise, move one step forward.

def turn_right():
    """Turn Reeborg to the right."""
    turn_left()
    turn_left()
    turn_left()
    
def change_direction():
    """Turn right and take one step."""
    turn_right()
    move()
    
while not at_goal():
    if front_is_clear() and right_is_clear():
        change_direction()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif wall_in_front() and right_is_clear():
        change_direction()
    else:
        move()

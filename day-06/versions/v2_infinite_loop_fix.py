# TODO 1: Keep turn_right() from the first version: three left turns, with a docstring.

# TODO 2: Keep change_direction() from the first version: turn right, then move one step, with a docstring.

# TODO 3: Before the maze loop, move forward while the front is clear, then turn left.
#   Nudge: an open start with a clear right side makes the first version turn right forever. Walking to a wall
#   and turning left puts that wall on Reeborg's right.

# TODO 4: Loop until Reeborg is at the goal.

# TODO 5: If the front is clear and the right is clear, call change_direction().

# TODO 6: If there is a wall on the right and a wall in front, turn left.

# TODO 7: If there is a wall in front and the right is clear, call change_direction().

# TODO 8: Otherwise, move one step forward.

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
    if front_is_clear() and right_is_clear():
        change_direction()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif wall_in_front() and right_is_clear():
        change_direction()
    else:
        move()

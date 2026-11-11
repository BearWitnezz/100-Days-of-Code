# TODO 1: This file runs in Reeborg's World. turn_left, move, front_is_clear, right_is_clear, wall_in_front, and
#   at_goal already exist there. Reeborg has no turn_right, so define turn_right() with a docstring.
#   Nudge: a right turn is three left turns.

# TODO 2: Define change_direction() with a docstring. It turns right, then takes one step.

# TODO 3: Before the maze loop, move forward while the front is clear, then turn left.
#   Nudge: that puts a wall on Reeborg's right, so an open start cannot spin in a square forever.

# TODO 4: Loop until Reeborg is at the goal.

# TODO 5: If the right side is clear, call change_direction().

# TODO 6: Otherwise, if there is a wall in front, turn left.

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

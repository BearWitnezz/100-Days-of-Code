# TODO 1: turn_right() and change_direction() stay the same as the previous version. This file only shows the
#   main program.

# TODO 2: Before the maze loop, move forward while the front is clear, then turn left.

# TODO 3: Loop until Reeborg is at the goal.

# TODO 4: If the right side is clear, call change_direction().
#   Nudge: that one check covers both of the old "right is clear" branches.

# TODO 5: Otherwise, if there is a wall on the right and a wall in front, turn left.

# TODO 6: Otherwise, move one step forward.

while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        change_direction()
    elif wall_on_right() and wall_in_front():
        turn_left()
    else:
        move()

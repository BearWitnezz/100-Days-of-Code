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

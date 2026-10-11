def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def change_direction():
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

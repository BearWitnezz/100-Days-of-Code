def turn_right():
    turn_left()
    turn_left()
    turn_left()

def change_direction():
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

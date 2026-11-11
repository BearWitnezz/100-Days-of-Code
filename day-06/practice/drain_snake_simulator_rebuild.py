# TODO 1: Hide a clog a random 1 to 10 feet down the drain.
# TODO 2: Define push to show the snake's position, and twist to clear the clog only at that spot.
# TODO 3: Keep asking push or twist until twist clears the clog.

import random
clog_distance = random.randint(1,10)
snake_position = 0
clog_cleared = False
def push():
    """Print how far the snake has moved."""
    print(snake_position)
def twist():
    """Clear the drain when the snake has reached the clog."""
    if snake_position == clog_distance:
        print("Drain cleared!")
    else:
        print("Nothing here, keep pushing")

print("Welcome to the Drain Snake Simulator")
while not clog_cleared:
    push_or_twist = input("Push or Twist?\n").lower()
    if push_or_twist == "push":
        snake_position += 1
        push()
    elif push_or_twist == "twist":
        twist()
        if snake_position == clog_distance:
            clog_cleared = True
    else:
        print("invalid input")

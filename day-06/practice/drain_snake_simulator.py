# TODO 1: Hide a clog a random 1 to 10 feet down the drain.
# TODO 2: Define push and twist.
# TODO 3: Keep asking push or twist until the clog is cleared. Twist works only at the clog.

import random
clog_distance = random.randint(1,10)
clog_cleared = False
snake_position = 0
def push():
    """Print how far the snake has moved."""
    print(snake_position)
def twist():
    """Announce that the drain is cleared."""
    print("Drain cleared!")

print("Welcome to the Drain Snake Simulator")
while not clog_cleared:
    push_or_twist = input("Push or Twist?\n").lower()
    if push_or_twist == "push":
        snake_position += 1
        push()
    elif push_or_twist == "twist":
        if snake_position == clog_distance:
            twist()
            clog_cleared = True
        else:
            print("Nothing here, keep pushing.")
    else:
        print("invalid input!")

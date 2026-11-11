# TODO 1: Import random. Hide the clog a random 1 to 10 feet down the drain. Start the snake at 0 feet, and start
#   clog_cleared as False.

# TODO 2: Define push() with a docstring. It prints how far the snake has moved.

# TODO 3: Define twist() with a docstring. If the snake is at the clog, print "Drain cleared!". Otherwise print
#   "Nothing here, keep pushing".

# TODO 4: Print "Welcome to the Drain Snake Simulator".

# TODO 5: Loop while the clog is not cleared. Ask "Push or Twist?" and lowercase the answer.

# TODO 6: "push" adds 1 foot to the snake's position, then calls push().

# TODO 7: "twist" calls twist(). If the snake is sitting on the clog, set clog_cleared to True so the loop can stop.

# TODO 8: Any other answer prints "invalid input".

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

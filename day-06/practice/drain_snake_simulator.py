# TODO 1: Import random. Hide the clog a random 1 to 10 feet down the drain. Start the snake at 0 feet, and start
#   clog_cleared as False.

# TODO 2: Define push() with a docstring. It prints the snake's current position.

# TODO 3: Define twist() with a docstring. It prints "Drain cleared!".

# TODO 4: Print "Welcome to the Drain Snake Simulator".

# TODO 5: Loop while the clog is not cleared. Ask "Push or Twist?" and lowercase the answer.

# TODO 6: "push" moves the snake forward 1 foot, then calls push().

# TODO 7: "twist" clears the clog only when the snake's position equals the clog distance: call twist() and set
#   clog_cleared to True. Any other twist prints "Nothing here, keep pushing."

# TODO 8: Any other answer prints "invalid input!".

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

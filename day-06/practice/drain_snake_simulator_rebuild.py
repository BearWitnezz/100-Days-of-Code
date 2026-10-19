import random
clog_distance = random.randint(1,10)
snake_position = 0
clog_cleared = False
def push():
    print(snake_position)
def twist():
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

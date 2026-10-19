import random
clog_distance = random.randint(1,10)
clog_cleared = False
snake_position = 0
def push():
    print(snake_position)
def twist():
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

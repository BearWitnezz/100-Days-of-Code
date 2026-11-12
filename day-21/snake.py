# TODO 1: Create a Snake class. In __init__, make a list for the segments, call create_snake(), and after the snake is built, save the head as its own attribute (the first item in the list).

# TODO 2: Pull STARTING_POSITIONS, MOVE_DISTANCE, UP, DOWN, LEFT, and RIGHT out as ALL_CAPS constants at the top of the file.
#   Nudge: headings go counterclockwise from 0 (east): UP 90, DOWN 270, LEFT 180, RIGHT 0.

# TODO 3: create_snake() loops over STARTING_POSITIONS and builds each segment (white square, pen up, goto that position, append to the list).

# TODO 4: move() does the tail-follows-head loop (each segment goes to where the one ahead of it was, working back to front), then the head moves forward MOVE_DISTANCE.

# TODO 5: Add up, down, left, and right methods that turn the head with setheading, and don't let the snake reverse into itself.
#   Nudge: only change heading if it's not already going the opposite way. heading() is a method, so it needs parentheses.

# TODO 6: Pull the "create one segment at a position" code out of the create_snake loop into an add_segment(position) method. create_snake() just loops and calls self.add_segment(position).

# TODO 7: Add extend() that puts a new segment at the last segment's current position.
#   Nudge: the last item in a list is [-1], and position() is a method so it needs parentheses. One-sentence docstring on every function.

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Set up the snake object."""
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """Creates a new Snake object."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        """Does the tail-follow-head loop."""
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        """Moves the snake up."""
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake down."""
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake left."""
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake right."""
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        """Extends the snake."""
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        """Adds a new segment to the snake."""
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake.append(new_snake)

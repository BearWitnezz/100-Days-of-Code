from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """Creates a new Snake object."""
        for position in STARTING_POSITIONS:
            new_snake = Turtle()
            new_snake.shape("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snake.append(new_snake)

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

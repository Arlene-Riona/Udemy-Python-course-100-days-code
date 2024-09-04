from turtle import Turtle
INITIAL_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):
        for coordinate in INITIAL_COORDINATES:
            self.extend_snake(coordinate)

    def extend_snake(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_squares.append(snake)

    def inc_snake_length(self):
        self.extend_snake(self.all_squares[-1].position())

    def move(self):
        full_snake = self.all_squares
        for current_square in range(len(full_snake) - 1, 0, -1):
            # x and y coordinate of the previous square
            new_x_coordinate = full_snake[current_square - 1].xcor()
            new_y_coordinate = full_snake[current_square - 1].ycor()
            # moving the current square to the coordinates of the previous square
            full_snake[current_square].goto(x=new_x_coordinate, y=new_y_coordinate)
        self.head.forward(MOVE_FORWARD_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.all_squares:
            segment.goto(1000, 1000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]
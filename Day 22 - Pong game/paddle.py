from turtle import Turtle
PADDLE_DISTANCE = 10
MAX_LOWER_LIMIT = -240
MAX_UPPER_LIMIT = 250
paddle_list = []

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.coordinate_y_left = 0
        self.coordinate_y_right = 0
        block = Turtle("square")
        self.block = block
        block.penup()
        block.goto(position[0], position[1])
        block.shapesize(stretch_len=1, stretch_wid=5)
        block.color("white")
        paddle_list.append(block)

    def moving_up(self):
        if self.block.ycor() < MAX_UPPER_LIMIT:
            x = self.block.xcor()
            self.coordinate_y_left += PADDLE_DISTANCE
            y = self.coordinate_y_left
            self.block.goto(x, y)

    def moving_down(self):
        if self.block.ycor() > MAX_LOWER_LIMIT:
            x = self.block.xcor()
            self.coordinate_y_left -= PADDLE_DISTANCE
            y = self.coordinate_y_left
            self.block.goto(x, y)

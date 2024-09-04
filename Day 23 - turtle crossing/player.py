from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.showturtle()

    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def reset_position(self):
        self.hideturtle()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()
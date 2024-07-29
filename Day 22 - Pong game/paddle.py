from turtle import Turtle
INITIAL_POSITION = [(450, 0)]
paddle_list = []

class Paddle:
    def __init__(self):
        super().__init__()
        self.create_paddle()


    def create_paddle(self):
        block = Turtle("square")
        block.shapesize(stretch_len=20, stretch_wid=100)
        block.color("white")
        block.penup()



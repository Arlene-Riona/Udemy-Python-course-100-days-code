from turtle import Turtle

FONT = ("Courier", 24, "bold")
SCORE_POSITION = (-280, 240)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCORE_POSITION[0], SCORE_POSITION[1])
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(arg=f"Level:{self.level}", font=FONT)

    def update_level(self):
        self.level += 1

    def game_over(self):
        self.goto(-100, 0)
        self.write(arg="GAME OVER", font=FONT)


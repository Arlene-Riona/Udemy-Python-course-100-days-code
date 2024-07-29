from turtle import Turtle

LOCATION_X = 0
LOCATION_Y = 260
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(LOCATION_X, LOCATION_Y)
        text = f"Score: {self.score}"
        self.write(text, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        text = "GAME OVER"
        self.write(text, align=ALIGNMENT, font=FONT)

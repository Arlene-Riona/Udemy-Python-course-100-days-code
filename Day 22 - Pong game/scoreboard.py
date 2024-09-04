from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.goto(-200, 190)
        self.write(self.left_score, font=("Courier", 80, "normal"))
        self.goto(200, 190)
        self.write(self.right_score, font=("Courier", 80, "normal"))

    def update_left_scoreboard(self):
        self.left_score += 1
        self.display_scoreboard()

    def update_right_scoreboard(self):
        self.right_score += 1
        self.display_scoreboard()
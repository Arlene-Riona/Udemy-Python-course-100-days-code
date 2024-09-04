from turtle import Turtle

LOCATION_X = 0
LOCATION_Y = 260
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(LOCATION_X, LOCATION_Y)
        text = f"Score: {self.score} | High Score: {self.high_score}"
        self.write(text, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore()
        self.score = 0
        self.update_score()

    def inc_score(self):
        self.score += 1
        self.update_score()

    def read_highscore(self):
        file = open("data.txt", "r")
        data = file.read()
        score = int(data)
        file.close()
        return score

    def write_highscore(self):
        file = open("data.txt", "w")
        file.write(str(self.high_score))
        file.close()

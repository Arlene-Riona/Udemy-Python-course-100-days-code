from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.x = 10
        self.y = 10
        self.time_increment = 0.01
        self.current_sleep_time = 0.1

    def change_direction_along_y(self):
        self.y *= -1

    def change_direction_along_x(self):
        self.x *= -1
        self.sleep_time_ball_movement()

    def move(self):
        """This function moves the ball and changes direction upon collision"""
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        print("")
        print(f"Current coordinates ({new_x}, {new_y})")
        print("")
        self.goto(new_x, new_y)

    def reset_position_to_left(self):
        self.home()
        self.current_sleep_time = 0.1
        new_x = self.xcor() - self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def reset_position_to_right(self):
        self.home()
        self.current_sleep_time = 0.1
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def sleep_time_ball_movement(self):
        self.current_sleep_time = self.current_sleep_time - self.time_increment
        if self.current_sleep_time < 0.01:
            self.current_sleep_time = 0.01
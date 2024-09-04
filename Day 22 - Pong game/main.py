from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


def distance_calculator(point1, point2):
    import math
    dist = math.dist(point1, point2)
    return dist

def check_collision_with_paddle(ball, paddle):
    # Check for collision with a given paddle
    if paddle.xcor() - 20 < ball.xcor() < paddle.xcor() + 20 and paddle.ycor() - 50 < ball.ycor() < paddle.ycor() + 50:
        return True
    return False

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

left_paddle = Paddle((-450, 0))
right_paddle = Paddle((450, 0))

ball = Ball()
score = ScoreBoard()

#screen.bgpic("wall.png")
#screen.bgpic("wall2.png")
screen.listen()
screen.onkey(left_paddle.moving_up, "w")
screen.onkey(left_paddle.moving_down, "s")
screen.onkey(right_paddle.moving_up, "Up")
screen.onkey(right_paddle.moving_down, "Down")

game_status = True
while game_status:
    time.sleep(ball.current_sleep_time)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_along_y()

    if ball.xcor() > 350:
        print(distance_calculator([right_paddle.xcor(), right_paddle.ycor()], [ball.xcor(), ball.ycor()]))

        # detecting collision with the paddles
    if check_collision_with_paddle(ball, right_paddle):
        print("Collision with right paddle")
        ball.change_direction_along_x()

    if check_collision_with_paddle(ball, left_paddle):
        print("Collision with left paddle")
        ball.change_direction_along_x()
    """
        # detecting collision with the paddles
    if ball.xcor() > 420 and ball.distance(right_paddle) < 50:
        print("Collision with right paddle")
        ball.change_direction_along_x()

    if ball.xcor() < -420 and ball.distance(left_paddle) < 50:
        print("Collision with left paddle")
        ball.change_direction_along_x()
    """

    """
    # detecting collision with the paddle
    #print(f"{ball.distance(right_paddle) < 462} and {ball.xcor() > 430}")
    print(f"DIST:___{ball.distance(right_paddle)}")
    print(f"{433 <= ball.distance(right_paddle) < 500} and {ball.xcor() > 380} or {ball.distance(left_paddle) < 50} and {ball.xcor() < -320}")
    #if ball.distance(right_paddle) > 452 and ball.xcor() > 430 or ball.distance(left_paddle) < 469 and ball.xcor() < -430:
    if 433 <= ball.distance(right_paddle) < 500 and ball.xcor() > 380:# or ball.distance(left_paddle) < 50 and ball.xcor() < -430:
        print("HERE HERE HERE HERE!!!!")
        ball.change_direction_along_x()
    """
    if ball.xcor() > 490:
        # ball goes out of bound and moves to the centre of the screen
        score.update_left_scoreboard()
        ball.reset_position_to_left()
    if ball.xcor() < -490:
        score.update_right_scoreboard()
        ball.reset_position_to_right()


screen.exitonclick()

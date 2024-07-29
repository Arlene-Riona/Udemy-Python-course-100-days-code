from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
snake = Snake()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game!")
screen.tracer(0)

score = ScoreBoard()
food = Food()

# to start listening to any keystrokes from the user
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # to detect if the food is consumed by the snake (increases the length of the snake and updates the score)
    if snake.head.distance(food) < 15:
        food.food_position()
        snake.inc_snake_length()
        score.update_score()

    # to detect if the snake has hit the screen
    if snake.head.xcor() > 297 or snake.head.xcor() < -297 or snake.head.ycor() > 300 or snake.head.ycor() < -299:
        game_on = False
        score.game_over()

    # to detect if the snake has hit any of it's body parts
    for snake_part in snake.all_squares[1:]:
        if snake.head.distance(snake_part) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING!!!")
screen.bgpic("line2.png")
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")

game_is_on = True
increment = 0

while game_is_on:
    increment += 1
    time.sleep(0.1)
    score.display_level()
    if increment % 15 == 0:
        car.car_on_screen()
    if player.reach_finish_line():
        player.reset_position()
        car.speed_changer()
        score.update_level()
    for car_obj in car.all_cars:
        if car_obj.distance(player) < 25:
            # game over sequence
            game_is_on = False
            score.game_over()
    car.move_car()
    screen.update()

screen.exitonclick()
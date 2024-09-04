from turtle import Turtle
import random

COLORS = ["red", "orange", "pink", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
Y_COORDINATES = list(range(-230, 241, 30))


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.car_on_screen()

    def create_car(self, x, y):
        car_colour = random.choice(COLORS)
        new_car = Turtle("square")
        new_car.hideturtle()
        new_car.color(car_colour)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        new_car.goto(x, y)
        new_car.showturtle()
        self.all_cars.append(new_car)

    def car_on_screen(self):
        """Generates any number of cars from 1-7 each round."""
        for number in range(random.randint(1, 7)):
            x = random.randint(305, 309)
            # y = random.choice(Y_COORDINATES)
            y = random.randint(-230, 240)
            self.create_car(x, y)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def speed_changer(self):
        self.move_speed += MOVE_INCREMENT

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)

race_line = Turtle("triangle")
race_line.hideturtle()
race_line.pensize(5)
race_line.penup()
race_line.goto(360,-300)
race_line.setheading(90)
race_line.pendown()
race_line.forward(600)

colour_list = ["red", "green", "blue", "pink", "yellow"]

user_bet = screen.textinput(title="Enter your bet!", prompt="Enter the turtle colour that might win the race "
                                                 "(red/green/blue/pink/yellow) ")
y_coordinate = [-200, -100, 0, 100, 200]
racers = []

start = True
condition = True

for turtle_index in range(0, 5):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colour_list[turtle_index])
    racers.append(turtle)
    turtle.goto(x=-370, y=y_coordinate[turtle_index])

while start:
    for race_turtle in racers:
        if condition:
            race_turtle.forward(random.randint(0, 10))
            if race_turtle.xcor() > 360:
                condition = False
                start = False
                race_line.hideturtle()
                race_line.penup()
                race_line.goto(-360, 0)
                if user_bet.lower() == race_turtle.pencolor():
                    text = f"You have won the bet!!!\nYou had selected {user_bet.title()} Turtle."
                    race_line.write(text, font=("Verdana", 15, "normal"))
                else:
                    text = f"You lost :(\nYou had selected {user_bet.title()} Turtle.\n{race_turtle.pencolor().title()} Turtle is the winner!"
                    race_line.write(text, font=("Verdana", 15, "normal"))

screen.exitonclick()
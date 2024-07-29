from turtle import Turtle, Screen
import heroes

turtle = Turtle()
turtle.shape("triangle")
turtle.color("DeepPink2")

# drawing a 100x100 square
for no_of_times in range(4):
    turtle.forward(100)
    turtle.right(90)

# drawing a dashed line
for _ in range(25):
    turtle.forward(5)
    turtle.penup() # lifts the pen up
    turtle.forward(5)
    turtle.pendown() # places the pen down
    turtle.forward(5)


print(heroes.gen())

screen = Screen()
screen.exitonclick()
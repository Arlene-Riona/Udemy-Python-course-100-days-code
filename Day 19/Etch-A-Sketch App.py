from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def anti_clockwise():
    tim.left(20)


def clockwise():
    tim.right(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# from now on turtle will listen to all Key events
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=anti_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
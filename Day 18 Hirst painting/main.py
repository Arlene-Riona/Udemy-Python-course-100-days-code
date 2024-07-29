# import colorgram
#
# colours_list = []
# colours = colorgram.extract("image.jpg", 25)
# for colour_item in colours:
#     rgb = colour_item.rgb
#     colours_list.append((rgb.r, rgb.g, rgb.b))
#     # OR: r = colour_item.rgb.r, g = colour_item.rgb.g, b = colour_item.rgb.b
#     # OR: colours_list.append((rgb[0], rgb.[1], rgb.[2]))
#
# print(colours_list)


import turtle

hirst_colour_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
 (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41),
  (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72),
  (83, 147, 126), (181, 87, 90)]


turtle.colormode(255)
timmy = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=750, height=750)
screen.title("**___Hirst 1 million dollar painting!___**")
timmy.hideturtle()
timmy.shape("turtle")
timmy.penup()
timmy.goto(-200, -190)
timmy.speed("fast")


def moving_forward(colour_lst, distance, dot_size, no_of_times=1):
    """This functions makes the turtle to move and leave dots in different colours."""
    import random
    for movement in range(no_of_times):
        colour_of_dot = random.choice(hirst_colour_list)
        timmy.dot(dot_size, colour_of_dot)
        timmy.penup()
        timmy.forward(distance)


def change_in_direction(steps):
    """This function changes the direction of the turtle to left/right based on the steps."""
    if (steps + 1) % 2 == 0:
        timmy.penup()
        timmy.right(90)
    else:
        timmy.penup()
        timmy.left(90)


for steps in range(10):
    moving_forward(hirst_colour_list, 50, 20, 10)
    change_in_direction(steps)
    timmy.forward(50)
    change_in_direction(steps)
    timmy.forward(50)


screen.exitonclick()
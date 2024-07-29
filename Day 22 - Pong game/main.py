from turtle import Screen
from PIL import Image

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("PONG")
screen.bgcolor("black")
#
# with Image.open("wall.png") as wall:
#     (width, height) = (1000, 650)
#     wall_resized = wall.resize((width, height))
#
# wall.save("wall.png")
# wall.close()
screen.bgpic("wall.png")
screen.listen()




screen.exitonclick()

# import turtle, timmy = turtle.Turtle()
from turtle import Turtle, Screen

timmy = Turtle()
#print(timmy)
timmy.shape("turtle")

my_screen = Screen()
my_screen.canvheight
timmy.color("blue4")
timmy.forward(100)
my_screen.exitonclick()

from prettytable import PrettyTable #from the module your importing the class PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squartile", "Charmander"])
table.add_column("Type", ["electric", "water", "fire"])
table.align = "l" #to make change to an attribute, we need to use =
print(table)












#my_screen.done()
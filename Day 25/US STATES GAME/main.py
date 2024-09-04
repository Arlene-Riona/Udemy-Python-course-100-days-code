from tkinter import messagebox
import turtle
import pandas


def final_message(score):
    if score >= 45:
        return "You have an amazing knowledge about the US states! great job!!!"
    elif 25 <= score <= 44:
        return "Good job!!! play again to score more!"
    elif 15 <= score <= 24:
        return "Play again to score more! you can do it!"
    else:
        return "Play again to score more! I'm sure you can do much better next time :)"


EXIT_CONDITION = "done"
NUMBER_OF_STATES = 50
correct_guess = 0

us_data = pandas.read_csv("50_states.csv")
us_states_list = us_data.state.to_list()
user_guess_list = []

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
'''
# adds the "image" as a new shape to screen's shape list along with circle, square...
screen.addshape(image)
# as "image" is a new shape added, we can ask the turtle to use this as it's shape
#turtle.shape(image)
'''
turtle.penup()
turtle.hideturtle()

messagebox.showinfo(title="Welcome to US States Game!", message="Guess as many states in the US as you can "
                                                                "and when your done, type 'done' to end the "
                                                                "game and to know your score. Good luck!")
user_guess = screen.textinput(title="Guess the state!", prompt="Guess another name of the state")
user_guess = user_guess.title()

while user_guess.lower() != EXIT_CONDITION:
    if user_guess in us_states_list:
        correct_guess += 1
        user_guess_list.append(user_guess)
        us_states_list.remove(user_guess)
        x_coordinate = us_data[us_data.state == user_guess].x
        y_coordinate = us_data[us_data.state == user_guess].y
        # TO AVOID THE FOLLOWING WARNING: FutureWarning: Calling int on a single element Series is deprecated and
        # will raise a TypeError in the future. Use int(ser.iloc[0]) instead
        turtle.goto(int(x_coordinate.iloc[0]), int(y_coordinate.iloc[0]))
        turtle.write(arg=user_guess)
    elif user_guess in user_guess_list:
        messagebox.showinfo(message=f"You have already guessed {user_guess}.")
    else:
        messagebox.showinfo(title="Incorrect guess!", message=f"{user_guess} is not a state in the US :(")
    user_guess = screen.textinput(title=f"{correct_guess}/{NUMBER_OF_STATES} States Correct",
                                  prompt="Guess another name of the state")
    user_guess = user_guess.title()


messagebox.showinfo(message=f"Thanks for playing!\nYou have scored {correct_guess}/{NUMBER_OF_STATES}.\n"
                            f"{final_message(correct_guess)}")
turtle.goto(-130, 280)
turtle.write(arg="Here are all the states in the US!", font=("Arial", 14, "bold"))
turtle.speed("fastest")
turtle.pencolor("blue")
for unguessed_place in us_states_list:
    x_coordinate = us_data[us_data.state == unguessed_place].x
    y_coordinate = us_data[us_data.state == unguessed_place].y
    turtle.goto(int(x_coordinate.iloc[0]), int(y_coordinate.iloc[0]))
    turtle.write(arg=unguessed_place)

# creating a csv file for the states that were not guessed
dictionary = {
    "states": us_states_list
}
# dictionary being converted into a dataframe
data = pandas.DataFrame(dictionary)
data.to_csv("states_to_learn.csv")

screen.exitonclick()
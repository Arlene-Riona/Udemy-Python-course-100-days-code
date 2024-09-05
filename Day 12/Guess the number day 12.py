from GTN_Logo import *
import random

def high_or_low(user_number, random_num):
    if user_number > random_num:
        return "Too high."
    elif user_number < random_num:
        return "Too low."
    else:
        return f"You got it! The number was {random_num}."

def main_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    random_num = random.randint(1, 100)
    #print(random_num)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    guess_num = 6 #if the user selects the hard level
    flag_var = ""
    if level == "easy": #if level is easy
        guess_num = 10 
    print(f"You only have {guess_num} guesses!")
    print("I'm thinking of a number between 1 and 100.")

    while guess_num != 0:
        user_number = int(input("Make a guess: "))
        output = high_or_low(user_number, random_num)
        print(output)
        print(" ")
        if output == f"You got it! The number was {random_num}.":
            flag_var = " "
            print(you_win)
            break
        guess_num -= 1
        print(f"You have {guess_num} attempts remaining to guess the number.")
    if not flag_var:
        print("You have run out of guesses........")
        print(f"The number is {random_num}!")
    print(" ")
    print(the_end)

main_game()
from hangman_art import *

def country_generator():
    import random
    country_data = []
    file = open("C:\\Users\\arlen\\OneDrive\\Desktop\\UDST\\100 Days python code additional\\country list.txt", "r")
    for i in file:
        data = i.lower().strip()
        country_data.append(data)
    random_country = random.choice(country_data)
    return random_country

def printing_country_name(list1): #do only printing.
    for i in list1:
        print(i, end = " ")
    print()

print(logo)
print(" ")
country_to_guess = country_generator()
user_guess = list("_"*len(country_to_guess))
num_of_times = 7
lives = num_of_times
stage_counter = 6
print(f"Guess the country! ", end = "")
printing_country_name(user_guess)
print()
for i in range(num_of_times):
    x = True
    while x:
        try:
            print(" ")
            letter = input("Enter your guess (type a single letter): ").lower()
            assert len(letter) and letter.isalpha() == 1
            x = False
        except:
            print("Invalid input! please enter a letter only! try again......")
    copy_of_user_guess = user_guess.copy()
    for index in range(len(country_to_guess)):
        if letter == country_to_guess[index]:
            user_guess[index] = letter
    lives -= 1
    print(" ")
    printing_country_name(user_guess)
    print(" ")
    if lives != 0:
        if user_guess == copy_of_user_guess:
            if lives != 1:
                print(f"Letter {letter} is not in this word! you only have {lives} lives remaining.....")
            else:
                print(f"Letter {letter} is not in this word! you only have {lives} life remaining.....")
            print(stages[stage_counter])
            stage_counter -= 1
        else:
            if lives != 1:
                print(f"Great job! keep going ahead! you have still {lives} more lives!")
            else:
                print(f"Great job! keep going ahead! you have still {lives} more life!")
print(stages[stage_counter])
                
print(" ")
print(" ")
result = str(user_guess).strip()
if country_to_guess == result:
    print("Congradulations!! you won!")
else:
    print(f"You lost! the word was {country_to_guess.title()}! \nPlay again to win!")
print(" ")
print(" ")
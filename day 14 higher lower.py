from day14_game_data import * 
from day14_art import * 

# this function selects A and B for the user to guess 
def create_A_and_B(a = "", b = ""):
    '''This function creates the A and B for the game for the user to guess.
    INPUT PARAMETER: A and B which is a dictionary
    FUNCTION RETURN: returns A and B in a tuple.'''
    import random 
    if a == "":
        # use random module and get a person's data
        selected_data = random.choice(data)
        a = selected_data
    else:
        a = b
    b = random.choice(data)
    while b == a:
        b = random.choice(data)
    return a, b

# this function returns the option that has the most follower count 
def correct_ans(a, b):
    '''This function checks the dictionary and finds which dictionary has the most followers.'''
    if a['follower_count'] > b['follower_count']:
        return "A"
    else:
        return "B"

def score_counter(dict1, dict2, user_guess):
    correct_guess = correct_ans(dict1, dict2)
    if correct_guess == user_guess:
        return True
    else:
        return False

# main program
print(logo)
score = 0
A, B = create_A_and_B()
while True:
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    print(" ")
    result = score_counter(A, B, user_guess) 
    if result == False:
        break
    else:
        score += 1
    print("You're right! your current score is", score)
    print(" ")
    A, B = create_A_and_B(A, B)
print("You lost! your final score is", score)
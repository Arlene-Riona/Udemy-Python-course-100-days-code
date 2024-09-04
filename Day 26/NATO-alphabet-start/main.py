import pandas

# TODO 1. Create a dictionary in this format:
# converting the csv file into a dataframe
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# looping through the dataframe row by row
dictionary = {row.letter:row.code for index, row in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter your name: ")
letters = [i.upper() for i in user_name]
result = [dictionary[i] for i in letters]
print(result)
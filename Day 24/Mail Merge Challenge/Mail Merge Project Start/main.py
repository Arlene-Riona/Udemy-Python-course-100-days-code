#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# CODE STARTS HERE
TO_REPLACE = "[name]"

# READ THE LETTER TEMPLATE
template_file = open("./Input/Letters/starting_letter.txt", "r")
template_content = template_file.readlines()
template_file.close()

# READ THE LIST OF NAMES
name_file = open("./Input/Names/invited_names.txt", "r")
names = name_file.readlines()
name_file.close()

# REPLACE THE NAMES IN THE LETTER TEMPLATE AND SAVE TO ReadyToSend FOLDER
for invited_name in names:
    content = template_content.copy()
    striped_name = invited_name.strip()
    change = content[0].replace(TO_REPLACE, striped_name)
    content.insert(0, change)
    content.pop(1)
    # SAVING TO THE FOLDER
    with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", "w") as file:
        for item in content:
            file.write(item)

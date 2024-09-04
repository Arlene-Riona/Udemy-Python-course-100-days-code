# imports all classes and constants not modules
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
from statistics import mode

FONT_NAME = "Calibri"
FONT_SIZE = 18
dark_purple = "#180161"
orange = "#FB773C"
dark_blue = "#26355D"

# ---------------------------- FREQUENTLY USED EMAIL ---------------------------- #


def frequently_used_email():
    email_list = []
    with open("data.txt", "r") as data_file:
        for line in data_file:
            emails = line.split("|")[1].strip()
            only_email = emails[4:]
            email_list.append(only_email)
    frequent_email = mode(email_list)
    return frequent_email


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for char in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for char in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)

    random_password = "".join(password_list)
    password.delete(0, END)
    password.insert(0, random_password)
    # copies the text into clipboard
    pyperclip.copy(random_password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """This function takes all the data from the user and saves it into the file demo.txt"""
    website = website_name.get()
    user_id = username.get()
    user_pass = password.get()
    if len(website) == 0 or len(user_pass) == 0 or len(user_id) == 0:
        messagebox.showinfo(title="Oops!", message=f"Do not leave any of the fields empty!")
    else:
        display_message = f"These are the details entered:\nEmail: {user_id}\nPassword: {user_pass}\nIs it ok to save?"
        confirmation_from_user = messagebox.askokcancel(title=website.title(), message=display_message)
        if confirmation_from_user:
            with open("data.txt", "a") as file:
                data = f"Website: {website} | ID: {user_id} | Password: {user_pass}\n"
                file.write(data)
            website_name.delete(0, END)
            password.delete(0, END)
            username.delete(0, END)
            frequent_email = frequently_used_email()
            username.insert(0, frequent_email)


# ---------------------------- UI SETUP ------------------------------- #
# creating the root window
window = Tk()
window.title("Password Manager")
window.minsize(width=700, height=550)
window.config(padx=50, pady=50, background=dark_purple)

# creating logo.png appear on screen using canvas
logo_canvas = Canvas(height=200, width=189, highlightthickness=0, bg=dark_purple)
logo = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 94, image=logo)
logo_canvas.grid(column=1, row=0)

# creating labels, text boxes and buttons
website_label = Label(text="Website: ", font=(FONT_NAME, FONT_SIZE, "bold"), bg=dark_purple, fg=orange)
website_label.grid(column=0, row=1)

website_name = Entry(width=35, font=(FONT_NAME, FONT_SIZE, "normal"))
website_name.grid(column=1, row=1, columnspan=2, pady=10)
website_name.focus()

username_label = Label(text="Email/Username: ", font=(FONT_NAME, FONT_SIZE, "bold"), bg=dark_purple, fg=orange)
username_label.grid(column=0, row=2)

username = Entry(width=35, font=(FONT_NAME, FONT_SIZE, "normal"))
username.grid(column=1, row=2, columnspan=2, pady=10)
# having a default value inserted at index 0, END can be used in this context as well
frequent_email = frequently_used_email()
username.insert(0, frequent_email)

pass_label = Label(text="Password: ",font=(FONT_NAME, FONT_SIZE, "bold"), bg=dark_purple, fg=orange)
pass_label.grid(column=0, row=3)

password = Entry(width=19, font=(FONT_NAME, FONT_SIZE, "normal"))
password.grid(column=1, row=3, pady=10)

generate_pass_button = Button(text="Generate Password", font=(FONT_NAME, 14, "bold"), bg=dark_blue, fg=orange,
                              command=password_generator)
generate_pass_button.grid(column=2, row=3, padx=10)

add_button = Button(text="Add", font=(FONT_NAME, 14, "bold"), width=42, bg=dark_blue, fg=orange, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=10)


window.mainloop()
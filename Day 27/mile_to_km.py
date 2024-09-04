from tkinter import *

INTRO_FONT = ("Arial", 34, "bold")
MILE_TO_KM = 1.609344


def button_clicked():
    data = entry.get()
    result = round(float(data) * MILE_TO_KM, 4)
    display_km_label.config(text="")
    display_km_label.config(text=f"{result}")


window = Tk()
window.title("Mile to Km")
#window.minsize(width=600, height=400)
window.config(padx=50, pady=50)

# intro_label = Label(text="Mile to Km converter", font=INTRO_FONT)
# intro_label.grid(column=2, row=0)

entry = Entry(width=20)
entry.insert(END, string="Mile...")
entry.grid(column=2, row=2)

label1 = Label(text="Miles")
label1.grid(column=3, row=2)
#label1.config(padx=-500)

label2 = Label(text="is equal to")
label2.grid(column=1, row=4)

label3 = Label(text="Km")
label3.grid(column=3, row=4)

display_km_label = Label(text="0")
display_km_label.grid(column=2, row=4)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=6)

window.mainloop()
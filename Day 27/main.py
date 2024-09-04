import tkinter

window = tkinter.Tk()
window.title("My first program with GUI")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a label", font=("Arial", 34, "bold"))
label.grid(column=0, row=0)

def button_clicked():
    # get method needs to be tied to an event 
    data = text_box.get()
    label.configure(text=data)

def button_clicked2():
    # get method needs to be tied to an event
    print("Hello!")


text_box = tkinter.Entry(width=15)
text_box.grid(column=4, row=2)

button = tkinter.Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

button1 = tkinter.Button(text="New button!!", command=button_clicked2)
button1.grid(column=2, row=0)

window.mainloop()
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
PINK2 = "#FFD0D0"
RED = "#e7305b"
GREEN = "#468585"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_MIN = 1
# SHORT_BREAK_MIN = 1
# LONG_BREAK_MIN = 1
TICK = "✔️"
time_interval_count = 1
timer = None
marks = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global time_interval_count
    window.after_cancel(timer)
    timer_label.configure(text="Timer")
    tick_mark_label.configure(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    time_interval_count = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_timer():
    global time_interval_count
    # converting minutes to seconds
    if time_interval_count % 8 == 0:
        time_in_seconds = LONG_BREAK_MIN * 60
        timer_label.configure(text="20 minute break!", fg=RED)
    elif time_interval_count % 2 == 0:
        time_in_seconds = SHORT_BREAK_MIN * 60
        timer_label.configure(text="5 minute break", fg=PINK)
    else:
        time_in_seconds = WORK_MIN * 60
        timer_label.configure(text="WORK", fg=GREEN)
    time_interval_count += 1
    count_down(time_in_seconds)

# recursive function
def count_down(count):
    # the minute part of the time
    count_in_minute = count // 60
    # the seconds part of the time
    count_in_seconds = count % 60
    if len(str(count_in_seconds)) == 1:
        count_in_seconds = f"0{count_in_seconds}"
    # to make changes to the text of the canvas i.e. canvas.itemconfig(variable_name, changes to be made)
    canvas.itemconfig(timer_text, text=f"{count_in_minute}:{count_in_seconds}")
    if count >= 0:
        # happens after 1 second or 1000 millisecond
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global marks
        marks = ""
        work_sessions = math.floor(time_interval_count/2)
        for _ in range(work_sessions):
            marks += TICK
        tick_mark_label.configure(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=('Georgia', 40, "bold"), fg=GREEN, background=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, font=('Georgia', 12, "bold"), fg=RED, bg=PINK2)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",  command=reset_timer, font=('Georgia', 12, "bold"), fg=RED, bg=PINK2)
reset_button.grid(row=2, column=2)

tick_mark_label = Label(text="", font=('Georgia', 29, "bold"), fg=GREEN, background=YELLOW)
tick_mark_label.grid(row=3, column=1)

window.mainloop()
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 'None'

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    checkmark.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    window.focus_force()

    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        time = long_break_secs
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        time = short_break_secs
        title_label.config(text='Break', fg=PINK)
    else:
        time = work_secs
        title_label.config(text='Work', fg=GREEN)


    counter_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter_down(count):
    minutes = f'{math.floor(count/60)}'.rjust(2,'0')
    seconds = f'{count % 60}'.rjust(2,'0')

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')

    if count>0:
        global timer
        timer = window.after(1000, counter_down, count - 1)
    else:
        start_timer()
        checkmark.config(text=math.floor(reps/2)*'✔')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=2, row=1)

canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(125,125,image=img)

timer_text = canvas.create_text(125,140, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

start_button = Button(text='Start',background=YELLOW,highlightthickness=0,borderwidth=0,relief="flat",bd=0, command=start_timer)
start_button.grid(column=1,row=3)

reset_button = Button(text='Reset',background=YELLOW,highlightthickness=0,borderwidth=0,relief="flat",command=reset_timer)
reset_button.grid(column=3,row=3)

checkmark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'bold'))
checkmark.grid(column=2, row=4)

window.mainloop()
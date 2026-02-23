import json
import random
from tkinter import  *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial',60,'bold')
BASE_LANGUAGE = 'English'
LANGUAGE_TO_LEARN = 'French'
timer = ''

# Data handling
try:
    with open('./data/answered.json') as answered_file:
        answered_json = json.load(answered_file)
except FileNotFoundError:
    answered_json = {}
    pass

df = pd.read_csv('./data/french_words.csv')
all_words = {values[LANGUAGE_TO_LEARN]:values[BASE_LANGUAGE]
             for (key, values) in df.iterrows()
             if values[LANGUAGE_TO_LEARN] not in answered_json}

current_word = random.choice(list(all_words.items()))

# Timer mechanism
def start_timer(n):
    global timer
    if n >= 0:
        canvas.itemconfig(timer_count, text=n)
        timer = window.after(1000, start_timer, n - 1)
    else:
        reveal_answer()

# Core
def begin():
    print(len(all_words))
    show_random_word()
    start_timer(3)
    show_timer()

def show_random_word():
    global current_word
    temp = random.choice(list(all_words.items()))
    if temp != current_word:
        current_word = temp

    canvas.itemconfig(canvas_bg, image=card_front)
    canvas.itemconfig(title_label, text=LANGUAGE_TO_LEARN)
    canvas.itemconfig(word_label, text=current_word[0])

def reveal_answer():
    window.after_cancel(timer)
    hide_timer()
    canvas.itemconfig(canvas_bg, image=card_back)
    canvas.itemconfig(title_label, text=BASE_LANGUAGE)
    canvas.itemconfig(word_label, text=current_word[1])

def hide_timer():
    canvas.itemconfig(timer_count, state='hidden')
    canvas.itemconfig(timer_container, state='hidden')

def show_timer():
    canvas.itemconfig(timer_count, state='normal')
    canvas.itemconfig(timer_container, state='normal')

def got_right():
    save_to_json()
    all_words.pop(current_word[0])
    begin()

def got_wrong():
    begin()

def save_to_json():
    current_word_json = {current_word[0]:current_word[1]}
    try:
        with open('./data/answered.json', 'r') as answers_file:
            answers = json.load(answers_file)
    except FileNotFoundError:
        with open('./data/answered.json', 'w') as answers_file:
            json.dump(current_word_json, answers_file, indent=2)
    else:
        answers.update(current_word_json)
        with open('./data/answered.json', 'w') as answers_file:
            json.dump(answers, answers_file, indent=2)

# UI Setup
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
btn_right = PhotoImage(file='./images/right.png')
btn_wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=1,row=1,columnspan=2)
# canvas.create_image(400, 263, image=card_back)

canvas_bg = canvas.create_image(400, 263, image=card_front)
title_label = canvas.create_text(400, 150, text='Title', font=TITLE_FONT, fill='black')
word_label = canvas.create_text(400, 263, text='Word', font=WORD_FONT, fill='black')
timer_container = canvas.create_oval(650,30,750,130, fill='#eee', )
timer_count = canvas.create_text(702, 80, text='0', font=WORD_FONT, fill='#333')

btn_1 = Button()
btn_1.config(image=btn_wrong, borderwidth=0, highlightthickness=0,command=got_wrong)
btn_1.grid(column=1,row=2)

btn_2 = Button()
btn_2.config(image=btn_right, borderwidth=0, highlightthickness=0, command=got_right)
btn_2.grid(column=2,row=2)

begin()

window.mainloop()
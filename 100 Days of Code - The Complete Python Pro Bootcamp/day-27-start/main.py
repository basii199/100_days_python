from tkinter import *

def button_click():
    label.config(text=entry.get())

window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

label = Label(text='Hello World!', font=('Arial', 20))
label.pack()

button = Button(text='Click me', command=button_click)
button.pack()

entry = Entry(width=10)
entry.pack()

window.mainloop()
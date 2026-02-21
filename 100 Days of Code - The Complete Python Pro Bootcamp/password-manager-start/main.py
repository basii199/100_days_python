import json
from tkinter import *
from tkinter import messagebox
import random
from constants import letters,symbols,numbers

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def create_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)

    return password

def generate_password():
    pw = create_password()
    password_entry.delete(0, END)
    password_entry.insert(0, pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    json_entry = {website: {
        'email': email,
        'password': password
    }}

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title='Oops', message='You left a field empty')
        return

    is_ok = messagebox.askokcancel(title=website,
                           message=f'Confirm username and password\n\n'
                                                  f'Username: {email}\n'
                                                  f'Password: {password}')
    if is_ok:
        # with open('passwords.txt', 'a') as pw_file:
        #     pw_file.write(f'{website} | {email} | {password} \n')
        try:
            with open('passwords.json', 'r') as pw_file:
                content = json.load(pw_file)
        except FileNotFoundError:
            with open('passwords.json', 'w') as pw_file:
                json.dump(json_entry, pw_file, indent=2)
        else:
            content.update(json_entry)

            with open('passwords.json', 'w') as pw_file:
                json.dump(content, pw_file, indent=2)
        finally:
            # email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.delete(0, END)

            website_entry.focus()

# ----------------------------- SEARCH -------------------------------- #
def search_passwords():
    website = website_entry.get()
    try:
        with open('passwords.json', 'r') as pw:
            content = json.load(pw)
            messagebox.showinfo(title=website, message=f'Website: {website} \n\n'
                                                       f'Email: {content[website]['email']}\n'
                                                       f'Password: {content[website]['password']}')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found')
    except KeyError:
        messagebox.showinfo(title='Error', message='Website not found')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200,height=200, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(row=1,column=2)

website_label = Label()
website_label.config(text='Website:')
website_label.grid(row=2, column=1)

email_label = Label()
email_label.config(text='Email/Username:')
email_label.grid(row=3, column=1)

password_label = Label()
password_label.config(text='Password:')
password_label.grid(row=4, column=1)

website_entry = Entry()
website_entry.config(width=21)
website_entry.focus()
website_entry.grid(row=2,column=2)

email_entry = Entry()
email_entry.config(width=35)
email_entry.grid(row=3,column=2,columnspan=2)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=4,column=2)

search_button = Button()
search_button.config(text='Search', width=9, command=search_passwords)
search_button.grid(row=2,column=3)

generate_button = Button()
generate_button.config(text='Generate Password', width=9, command=generate_password)
generate_button.grid(row=4,column=3)

add_button = Button()
add_button.config(text='Add', width=33, command=save_password)
add_button.grid(row=5,column=2, columnspan=2)


window.mainloop()

#Based off Day 29 from Udemy 100 Days of Code

from random import choice, randint, shuffle
import os.path
from tkinter import *
from tkinter import messagebox
#Show user their passwords by reading passwords_managed.txt
def show_passwords():
    with open(file='/Users/finneassensiba/passwords_managed.txt', mode='r') as file:
        passwords = file.readlines()
        for line in passwords:
            print(line)
        file.close()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= randint(1, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)
    letters_list = [choice(letters) for n in range(nr_letters)]
    numbers_list = [choice(numbers) for n in range(nr_numbers)]
    symbols_list = [choice(symbols) for n in range(nr_symbols)]
    
    password_lst = letters_list + numbers_list + symbols_list
    shuffle(password_lst)
    password_final = "".join(password_lst)
    password_box.insert(0, password_final)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    path = '/Users/finneassensiba/passwords_managed.txt'
    new_website = website_box.get()
    new_email = email_box.get()
    new_password = password_box.get()
    if len(new_website) == 0 or len(new_email) == 0:
        fields_empty = messagebox.showerror(message='Missing data! Please fill out the entire form:)')
    else:
        isok = messagebox.askokcancel(title=new_website, message=f'These are the new details to be entered: \n{new_website}\n{new_email}\n{new_password}/nOK?')
        if isok:
            if os.path.isfile(path) is False:
                with open('/Users/finneassensiba/passwords_managed.txt', mode='w') as passwords:
                    passwords.write(f'{new_website} | {new_email} | {new_password}\n')
                    passwords.close()
            else:
                with open('/Users/finneassensiba/passwords_managed.txt', mode='a+') as passwords:
                    passwords.write(f'\n{new_website} | {new_email} | {new_password}')
                    passwords.close()
    password_box.delete(0, END)
    website_box.delete(0, END)
    email_box.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Local Password Manager & Generator')
window.config(padx=40, pady=40)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='/Users/finneassensiba/pystuff/password-manager-start/logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_box = Entry(width=35)
website_box.grid(row=1, column=1, columnspan=2)
website_box.focus()
#website_box.insert(0, 'your username or email')

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_box = Entry(width=35)
email_box.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_box = Entry(width=21)
password_box.grid(row=3, column=1)

generate_button = Button(text='Create Password', command=create_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add to passwords', width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

show_me_button = Button(text='Show me my passwords', width=36, command=show_passwords)
show_me_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
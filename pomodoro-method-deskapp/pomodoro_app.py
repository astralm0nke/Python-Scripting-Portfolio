#Based off 100 Days of Code- Day 28 on Udemy
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#hexcodes from colorhunt.io
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

#Guts
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_marks.config(text='Rounds: ')
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='Long Break:)', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        timer_label.config(text='Short Break!', fg=PINK)
    else:
          countdown(WORK_MIN * 60)
          timer_label.config(text='Work Sesh! :)', fg=GREEN)

def countdown(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = '00'
    elif count_seconds <= 9:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in math.floor(range(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)

# User Interface
window = Tk()
window.title('Pomodoro Productivity App')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='/Users/finneassensiba/pystuff/pomodoro-method-app/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', bg=YELLOW, font=(FONT_NAME, 50), fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text='Rounds:', font=25, fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
#Typing Speed Test
#I got the idea for the timer from SarahDev on Medium https://medium.com/@sarahisdevs/how-to-create-a-countdown-timer-using-python-6a09fea53e67

import tkinter as tk
import random

window = tk.Tk()
window.title('Typing Speed Test!')

wordbank = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Maecenas', 'a', 'dolor', 'vel', 'leo', 'mattis', 'placerat.', 'Cras', 'eget', 'venenatis', 'est.', 'Vivamus', 'magna', 'quam,', 'rhoncus', 'et', 'lacinia', 'vitae,', 'commodo', 'efficitur', 'lorem.', 'Morbi', 'ornare', 'et', 'leo', 'ut', 'pellentesque.', 'Praesent', 'efficitur', 'pretium', 'felis,', 'vitae', 'congue', 'magna.', 'Pellentesque', 'eu', 'est', 'nulla.', 'Curabitur', 'id', 'dolor', 'aliquet,', 'porta', 'ex', 'a,', 'sollicitudin', 'leo.', 'Nulla', 'ut', 'est', 'eget', 'tellus', 'congue', 'venenatis', 'at', 'eu', 'magna.', 'Sed', 'eget', 'risus', 'ut', 'dolor', 'tincidunt', 'rutrum', 'et', 'dapibus', 'elit.', 'Nulla', 'gravida', 'magna', 'libero,', 'sed', 'aliquam', 'est', 'dignissim', 'nec.', 'Sed', 'blandit', 'risus', 'lectus,', 'vel', 'iaculis', 'sapien', 'commodo', 'nec.', 'Suspendisse', 'quis', 'lacinia', 'nibh.', 'Morbi', 'augue', 'risus,', 'iaculis', 'sed', 'commodo', 'quis,', 'auctor', 'in', 'odio.', 'Vestibulum', 'pellentesque', 'aliquet', 'lacus,', 'vitae', 'blandit', 'lectus', 'iaculis', 'sit', 'amet.', 'Cras', 'malesuada', 'dignissim', 'erat,', 'nec', 'consectetur', 'lorem', 'convallis', 'vel.', 'Donec', 'vitae', 'ex', 'porta,', 'euismod', 'purus', 'ut,', 'pretium', 'tortor.', 'Proin', 'metus', 'turpis,', 'porta', 'at', 'tristique', 'ac,', 'viverra', 'nec', 'dolor.', 'Vestibulum', 'id', 'metus', 'sit', 'amet', 'metus', 'sodales', 'efficitur.', 'Proin', 'sit', 'amet', 'arcu', 'felis.', 'Pellentesque', 'tempor', 'lectus', 'eu', 'lectus', 'suscipit,', 'eget', 'posuere', 'lorem', 'euismod.', 'Nulla', 'eleifend', 'felis', 'nisi.', 'Aenean', 'egestas', 'nulla', 'sollicitudin', 'metus', 'maximus', 'fermentum.', 'Ut', 'in', 'volutpat', 'arcu,', 'et', 'rhoncus', 'tellus.', 'Fusce', 'non', 'pretium', 'nisl,', 'ac', 'hendrerit', 'lorem.', 'Praesent', 'a', 'nisi', 'sit', 'amet', 'nunc', 'malesuada', 'tempus', 'sit', 'amet', 'et', 'libero.', 'Sed', 'molestie', 'orci', 'nibh,', 'a', 'auctor', 'diam', 'ultrices', 'eu.', 'In', 'venenatis', 'ligula', 'neque,', 'et', 'vulputate', 'sem', 'tempor', 'ut.', 'Nunc', 'consequat', 'ipsum', 'in', 'leo', 'semper', 'gravida.', 'Pellentesque', 'pellentesque', 'semper', 'libero,', 'id', 'finibus', 'neque', 'congue', 'quis.', 'Vivamus', 'varius', 'sodales', 'tortor,', 'et', 'finibus', 'magna.', 'Vestibulum', 'neque', 'sapien,', 'iaculis', 'eu', 'luctus', 'eu,', 'sagittis', 'eu', 'lacus.', 'Aliquam', 'iaculis', 'sit', 'amet', 'odio', 'vel', 'hendrerit.', 'Class', 'aptent', 'taciti', 'sociosqu', 'ad', 'litora', 'torquent', 'per', 'conubia', 'nostra,', 'per', 'inceptos', 'himenaeos.', 'Praesent', 'tristique', 'auctor', 'blandit.', 'Suspendisse', 'et', 'odio', 'nibh.', 'Aliquam', 'maximus', 'orci', 'diam,', 'sit', 'amet', 'ultrices', 'magna', 'viverra', 'eu.', 'Donec', 'aliquam', 'faucibus', 'fermentum.', 'Phasellus', 'rutrum', 'egestas', 'mi,', 'ut', 'pretium', 'lacus', 'vehicula', 'ut.', 'Aliquam', 'bibendum', 'neque', 'est,', 'vulputate', 'gravida', 'orci', 'egestas', 'id.', 'Donec', 'auctor', 'sollicitudin', 'maximus.', 'Aenean', 'elit', 'nisi,', 'lobortis', 'sit', 'amet', 'sagittis', 'et,', 'pharetra', 'a', 'dolor.', 'In', 'vitae', 'ornare', 'lectus,', 'sed', 'hendrerit', 'risus.', 'Praesent', 'molestie', 'eleifend', 'lectus', 'sit', 'amet', 'porttitor.', 'Vestibulum', 'tincidunt', 'porttitor', 'risus,', 'in', 'pretium', 'mi', 'posuere', 'in.', 'Curabitur', 'eget', 'porta', 'nulla.', 'Proin', 'sagittis', 'nunc', 'a', 'tellus', 'venenatis', 'eleifend.', 'Vivamus', 'ac', 'fermentum', 'erat,', 'egestas', 'pretium', 'orci.', 'Quisque', 'quis', 'auctor', 'ex.', 'Aliquam', 'hendrerit', 'rutrum', 'enim', 'a', 'auctor.', 'In', 'volutpat', 'fringilla', 'justo', 'non', 'iaculis.', 'Nunc', 'faucibus', 'tristique', 'maximus.', 'Morbi', 'ultrices,', 'urna', 'eu', 'semper', 'egestas,', 'enim', 'ligula', 'mattis', 'risus,', 'eget', 'dictum', 'elit', 'ligula', 'et', 'ipsum.', 'Donec', 'eget', 'sem', 'ligula.', 'Praesent', 'sit', 'amet', 'velit', 'eget', 'diam', 'aliquet', 'facilisis', 'quis', 'pellentesque', 'enim.', 'Donec', 'ac', 'lorem', 'ex.', 'Integer', 'convallis', 'est', 'ac', 'quam', 'iaculis,', 'eget', 'sagittis', 'massa', 'egestas.', 'Nunc', 'a', 'finibus', 'enim.', 'Duis', 'hendrerit', 'maximus', 'est,', 'et', 'mollis', 'augue.', 'Nunc', 'a', 'nunc', 'ac', 'tellus', 'placerat', 'venenatis.', 'Nulla', 'vitae', 'elit', 'ornare,', 'accumsan', 'ante', 'at,', 'mattis', 'lectus.', 'Fusce', 'et', 'ligula', 'ut', 'nulla', 'laoreet', 'lacinia.', 'Suspendisse', 'eget', 'mattis', 'ex.', 'Nam', 'a', 'semper', 'magna,', 'a', 'placerat', 'orci.', 'Aenean', 'eleifend', 'egestas', 'enim', 'nec', 'pulvinar.', 'Donec', 'scelerisque', 'ipsum', 'a', 'gravida', 'placerat.', 'Nulla', 'id', 'diam', 'ut', 'turpis', 'laoreet.']

correct_words = 0
seconds = 60
test_word = tk.StringVar(value=random.choice(wordbank))

scoreboard = tk.Label(window, text=f'Correct Words: {correct_words}')
scoreboard.grid(row=0, column=0)

timeclock = tk.Label(window, text=f'Seconds: {seconds}')
timeclock.grid(row=1, column=0)

def results_popup(correct_words):
    popup = tk.Toplevel(window)
    popup.geometry("300x100")
    popup.title("Results")
    tk.Label(popup, text= f"{correct_words} words per minute!", font=('Mistral 18 bold')).place(x=150,y=80)

def run_test(seconds):
    if seconds >= 0:
        timeclock.config(text=f'Seconds: {seconds}')
        window.after(1000, lambda: run_test(seconds - 1))
    else:
        timeclock.config(text='Time\'s Up!')
        results_popup(correct_words)

def check_word(test_word, correct_words):
    if TypeBox.get() == test_word.get():
        correct_words += 1
        scoreboard.config(text=f'Correct Words: {correct_words}')
        WordDisplay.config(text='Correct!')
    else:
        WordDisplay.config(text='Try Again!')
        
    test_word.set(random.choice(wordbank))
    return correct_words

def update_score():
    global correct_words
    correct_words = check_word(test_word, correct_words)

WordDisplay = tk.Label(window, textvariable=test_word)
WordDisplay.grid(row=2, column=0)

TypeBox = tk.Entry(window)
TypeBox.grid(row=3, column=0)

StartButton = tk.Button(window, text='Start Test! >:)', command=lambda: run_test(seconds))
StartButton.grid(row=2, column=1)

CheckAnswer = tk.Button(window, text='Check Answer!', command=lambda: update_score())
CheckAnswer.grid(row=3, column=1)

window.mainloop()


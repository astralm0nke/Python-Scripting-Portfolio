from tkinter import *
import requests
#Based on Day 32 from App Brewery's Python Pro Bootcamp
def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    ye_quote = data['quote']
    canvas.itemconfig(quote_text, text=ye_quote)


window = Tk()
window.title("THUS SPAKE YE...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/Users/finneassensiba/pystuff/100_days/kanye-quotes-app/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="What will Ye say???", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="/Users/finneassensiba/pystuff/100_days/kanye-quotes-app/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()

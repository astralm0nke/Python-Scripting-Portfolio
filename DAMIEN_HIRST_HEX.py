import turtle as t
import random

def Damien_Hirst():
    print("SHEEESH!!! Famous contemporary artist Damien Hirst has been trapped in the body of a turtle by a dark hex!!!:( \nHe is condemned to make million dollar dot paintings for us for all eternity. :/)")
    number_of_dots = int(input("How many dots should Damien paint? "))
    t.colormode(255)
    screen = t.Screen()
    Damien = t.Turtle()
    Damien.penup()

    Damien.setheading(225)
    Damien.forward(300)
    Damien.setheading(0)

    Damien.shape('turtle')
    Damien.color('green')
    Damien.speed('fast')

    def colors():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    for dot in range(1, number_of_dots + 1):
        Damien.dot(20, colors())
        Damien.forward(50)
        if dot % 10 == 0:
            Damien.setheading(90)
            Damien.forward(50)
            Damien.setheading(180)
            Damien.forward(500)
            Damien.setheading(0)
    Damien.hideturtle()
    screen.exitonclick

Damien_Hirst()
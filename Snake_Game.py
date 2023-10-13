from turtle import Screen, Turtle
import time
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("My Snake Game")
screen.tracer(0)
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0,0), (-20,0), (-40,0)]
game_is_on  = True

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color('white')
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)
        self.head.forward(move_distance)
    
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(RIGHT)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(x=randx, y=randy)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align='center', font=("arial", 24, "normal"))
        self.hideturtle()

    def inc_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=("arial", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align='center', font=('arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()
        print("mMMmm nomnomnom")
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            scoreboard.reset()
            snake.reset()
            
screen.exitonclick()
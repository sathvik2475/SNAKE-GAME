import turtle
import time
import random

# Score board
delay = 0.1
score = 0
highscore = 0

# Setting up the screen
sn = turtle.Screen()
sn.title("Snake Game")
sn.bgcolor("blue")
sn.setup(width=600, height=600)
sn.tracer(0)

# Snake head
s_head = turtle.Turtle()
s_head.shape("square")
s_head.color("white")
s_head.penup()
s_head.goto(0, 0)
s_head.direction = "stop"

# Food
s_food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
s_food.speed(0)
s_food.shape(shapes)
s_food.color(colors)
s_food.penup()
s_food.goto(0, 100)

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

# Functions for snake directions
def goup():
    if s_head.direction != "down":
        s_head.direction = "up"

def godown():
    if s_head.direction != "up":
        s_head.direction = "down"

def goleft():
    if s_head.direction != "right":
        s_head.direction = "left"

def goright():
    if s_head.direction != "left":
        s_head.direction = "right"

def move():
    if s_head.direction == "up":
        y = s_head.ycor()
        s_head.sety(y + 20)
    if s_head.direction == "down":
        y = s_head.ycor()
        s_head.sety(y - 20)
    if s_head.direction == "left":
        x = s_head.xcor()
        s_head.setx(x - 20)
    if s_head.direction == "right":
        x = s_head.xcor()
        s_head.setx(x + 20)

# Keyboard bindings
sn.listen()
sn.onkeypress(goup, "w")
sn.onkeypress(godown, "s")
sn.onkeypress(goleft, "a")
sn.onkeypress(goright, "d")

segments = []

# Main game loop
while True:
    sn.update()

    # Check for collision with the border
    if s_head.xcor() > 290 or s_head.xcor() < -290 or s_head.ycor() > 290 or s_head.ycor() < -290:
        time.sleep(1)
        s_head.goto(0, 0)
        s_head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        
        score = 0
        delay = 0.1
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("candara", 24, "bold"))

    # Check for collision with food
    if s_head.distance(s_food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        s_food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        
        if score > highscore:
            highscore = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("candara", 24, "bold"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = s_head.xcor()
        y = s_head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with the body segments
    for segment in segments:
        if segment.distance(s_head) < 20:
            time.sleep(1)
            s_head.goto(0, 0)
            s_head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            
            score = 0
            delay = 0.1
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

sn.mainloop()

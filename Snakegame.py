import turtle
import time
import random

delay=0.1

# Score
score = 0
high_score = 0

# Window creation
win=turtle.Screen()
win.title("Old Snake's Game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0) #turns off the screen u updates

#Snakehead
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,100)
head.direction="stop"

#snakefood
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("turtle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

#moving head pos
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

#keyboard bindings
win.listen()
win.onkey(go_up,"w")
win.onkey(go_down,"s")
win.onkey(go_left,"a")
win.onkey(go_right,"d")

#main game loop
while True:
    win.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segment list
        segment.clear()

        #reset the Score
        score=0

        #reset the delay
        delay=0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random position on Screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001

        #increase the score
        score += 10

        if score > high_score:
            high_score=score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #move the end segment in the reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

win.mainloop()

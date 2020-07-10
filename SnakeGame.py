import turtle
import time
import random

bodySegments=[]

delay=0.1
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.setup(width=700,height=700)
screen.tracer(0)

#score
score=0
highScore=0

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 high score:0", align="center",font=("Courier",24,"normal"))

#Snake head
snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction="stop"

#Snake Food
Food=turtle.Turtle()
Food.speed(0)
Food.shape("circle")
Food.color("yellow")
Food.penup()
Food.goto(0,200)
#Snake Function
def goUp():
    if snake.direction!="down":
        snake.direction="up"

def goDown():
    if snake.direction != "up":
        snake.direction="down"

def goRight():
    if snake.direction != "left":
        snake.direction="right"

def goLeft():
    if snake.direction != "right":
        snake.direction="left"

def move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)


#Keys
screen.listen()
screen.onkeypress(goUp,"w")
screen.onkeypress(goDown,"s")
screen.onkeypress(goLeft,"a")
screen.onkeypress(goRight,"d")

#Main loop
while True:
    screen.update()
    #Check for a collision with the border
    if snake.xcor()>340 or snake.xcor()<-340 or snake.ycor()>340 or snake.ycor()<-340:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction="stop"

        #hide the body segments
        for segments in bodySegments:
            segments.goto(1000,1000)

        #clear the body segments
        bodySegments.clear()

        #Reset the score
        score=0
        #Reset the delay
        delay=0.1
        #update the score display
        pen.clear()
        pen.write("Score: {} High Score :{}".format(score, highScore), align="center",font=("Courier",24,"normal"))


    #Snake eats food
    if snake.distance(Food)<20:
        x=random.randint(-340,340)
        y=random.randint(-340,340)
        Food.goto(x,y)

        #Growing the snake body
        newbodySegment=turtle.Turtle()
        newbodySegment.speed(0)
        newbodySegment.shape("square")
        newbodySegment.color("orange")
        newbodySegment.penup()
        bodySegments.append(newbodySegment)

        #shorten the delay
        delay-=0.001

        #increase the score
        score+=10

        if score> highScore:
            highScore=score

        pen.clear()
        pen.write("Score: {} High Score :{}".format(score,highScore),align="center",font=("Courier",24,"normal"))

    #joining the body segments with the snake in reverse order
    for index in range(len(bodySegments)-1,0,-1):
        x=bodySegments[index-1].xcor()
        y=bodySegments[index-1].ycor()
        bodySegments[index].goto(x,y)

    #Moving the body segment 0 to the snake's head
    if len(bodySegments)>0:
        x=snake.xcor()
        y=snake.ycor()
        bodySegments[0].goto(x,y)

    move()
    #Check for the Snake collision with its body
    for segment in bodySegments:
        if segment.distance(snake)<20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction="stop"

            # hide the body segments
            for segments in bodySegments:
                segments.goto(1000, 1000)

            # clear the body segments
            bodySegments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay=0.1
            # update the score display
            pen.clear()
            pen.write("Score: {} High Score :{}".format(score, highScore), align="center",font=("Courier", 24, "normal"))


    time.sleep(delay)




screen.mainloop()

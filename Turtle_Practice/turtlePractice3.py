#Random walk
import random
import turtle as tur
t = tur.Turtle()
t.pensize(12)

dist = 20

t.speed(0)
for _ in range(200):
    r=random.random()
    g=random.random()
    b=random.random()
    t.pencolor((r,g,b))
    rd = random.randint(0,3)
    if(rd==0):
        t.setheading(90)
        t.forward(dist)
    elif(rd==1):
        t.setheading(0)
        t.forward(dist)
    elif(rd==2):
        t.setheading(270)
        t.forward(dist)
    elif(rd==3):
        t.setheading(180)
        t.forward(dist)

screen = tur.Screen()
screen.exitonclick()
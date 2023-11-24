from turtle import *
t = Turtle()
t.shape("turtle")
t.pu()
t.goto(-200,0)
t.pd()
for i in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen = Screen()
screen.exitonclick()
import random
import turtle as tur

def draw(n):
    for _ in range(n):
        t.forward(100)
        t.right(360/n)

colors = ['aquamarine2','DarkOrange3','azure2','bisque2','cyan','DarkOrchid1','green1','goldenrod1','firebrick','khaki1']
n = len(colors)
t = tur.Turtle()
for i in range(3,11):
    color = colors[random.randint(0,n-1)]
    t.pencolor(color)
    draw(i)

screen = tur.Screen()
screen.exitonclick()
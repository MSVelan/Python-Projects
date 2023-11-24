import turtle as tur
t = tur.Turtle()

def moveforwards():
    t.forward(10)
def movebackwards():
    t.back(10)
def rotateleft():
    t.left(10)
def rotateright():
    t.right(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pd()
screen = tur.Screen()
screen.listen()
screen.onkeypress(key='w',fun=moveforwards)
screen.onkeypress(key='s',fun=movebackwards)
screen.onkeypress(key='a',fun=rotateleft)
screen.onkeypress(key='d',fun=rotateright)
screen.onkeypress(key='c',fun=clear)
screen.exitonclick()
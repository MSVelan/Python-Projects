from turtle import Turtle
STYLE = ('verdana',7,'normal')
class Showtext(Turtle):
    def __init__(self,txt,pos):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(pos)
        self.pd()
        self.write(txt,False,'center',STYLE)
    def clear(self):
        self.reset()
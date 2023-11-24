from turtle import Turtle
STYLE = ('verdana',12,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.refresh()
    def refresh(self):
        self.reset()
        self.hideturtle()
        self.pu()
        self.goto(-300,290)
        self.pd()
        self.write(f"Score:{self.score}",False,'center',STYLE)
    def onwin(self):
        self.pu()
        self.goto(0,0)
        self.pd()
        self.write("YOU WON")

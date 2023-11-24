from turtle import Turtle
STYLE = ("Courier", 14 , "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-230,250)
        self.pd()
        self.write(f"Level 1",False,'center',STYLE)
    def refresh(self,lev):
        self.clear()
        self.write(f"Level {lev}",False,'center',STYLE)
    def gameover(self):
        self.pu()
        self.goto(0,0)
        self.pd()
        self.write("GAME OVER",False,'center',STYLE)
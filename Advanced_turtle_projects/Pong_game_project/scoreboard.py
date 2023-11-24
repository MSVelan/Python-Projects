from turtle import Turtle
import time
STYLE = ('Courier',14,'normal')
class Scoreboard(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.no = 0
        self._pos = pos
        self.hideturtle()
        self.pencolor("white")
        self.pu()
        self.goto(pos)
        self.pd()
        self.update()

    def update(self):
        self.clear()
        self.pu()
        self.goto(self._pos)
        self.pd()
        self.write(f"{self.no}",False,"center",STYLE)
    def checkwin(self):
        if(self.no==10):
            return True
        return False
    def refreshwin(self,n):
        self.pencolor("white")
        self.pu()
        self.goto((0,0))
        self.pd()
        self.write(f"The Winner is Player {n}",False,'center',STYLE)
        self.pu()
        time.sleep(3)
        self.reset()
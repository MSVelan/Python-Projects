from turtle import Turtle
STYLE = ('Courier',14,'normal')
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto((-200,250))
        self.pd()
        self.pencolor("white")
        self.write("Player 1",False,'center',STYLE)
        self.pu()
        self.goto((200,250))
        self.pd()
        self.write("Player 2",False,'center',STYLE)
        self.drawline()
    def drawline(self):
        self.pu()
        self.goto((0,300))
        self.pensize(4)
        self.setheading(270)
        self.pd()
        while(self.ycor()>-300):
            self.forward(30)
            self.pu()
            self.forward(20)
            self.pd()



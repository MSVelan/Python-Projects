from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(pos)
        self.color("white")
    def up(self):
        self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        self.goto(self.xcor(),self.ycor()-20)
    
    def collisionwithball(self,ball):
        if(self.distance(ball)<=50 and (self.xcor()>340 or self.xcor()<-340)):
            return True
    
    
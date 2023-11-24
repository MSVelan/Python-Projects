from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
    def createBall(self):
        self.shape("circle")
        self.pu()
        self.color("white")
        self.shapesize(0.8,0.8)
        self.speed(1)

    def move(self,x,y):
        newx = self.xcor() + x
        newy = self.ycor() + y
        self.goto(newx,newy)
    
    def rightoutofbounds(self):
        if(self.xcor()>=380):
            return True
        return False
    def leftoutofbounds(self):
        if(self.xcor()<=-380):
            return True
        return False

    def rightwallbounce(self):
        if(self.distance(self.xcor(),280)<=12):
            return True
    def leftwallbounce(self):
        if(self.distance(self.xcor(),-280)<=12):
            return True
    
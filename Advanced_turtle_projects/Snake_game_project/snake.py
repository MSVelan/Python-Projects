from turtle import Turtle
STARTPOS = [(0,0),(-20,0),(-40,0)]
DIST = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for pos in STARTPOS:
            self.addSegment(pos)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(DIST)

    def up(self):
        if(self.head.heading() != 270):
            self.head.setheading(90)
    
    def down(self):
        if(self.head.heading() != 90):
            self.head.setheading(270)
    
    def left(self):
        if(self.head.heading() != 0):
            self.head.setheading(180)

    def right(self):
        if(self.head.heading() != 180):
            self.head.setheading(0)

    def collisionWithWall(self):
        if(self.head.distance(300,self.head.ycor())<8):
            return True
        elif(self.head.distance(-300,self.head.ycor())<8):
            return True
        if(self.head.distance(self.head.xcor(),300)<8):
            return True
        elif(self.head.distance(self.head.xcor(),-300)<8):
            return True
        return False
    
    def addSegment(self,pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.addSegment(self.segments[-1].position())
    
    def gamereset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]


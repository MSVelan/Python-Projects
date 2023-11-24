from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.level = 1
        self.allcars = []
    def createcar(self):
        choice = random.randint(1,6)
        if(choice==1):
            r = random.randint(-250,250)
            newturtle = Turtle("square")
            rcolor = random.choice(COLORS)
            newturtle.pu()
            newturtle.shapesize(stretch_len=2,stretch_wid=1)
            newturtle.fillcolor(rcolor)
            newturtle.goto(300,r)
            self.allcars.append(newturtle)
    def movecars(self):
        for i in self.allcars:
            i.backward(STARTING_MOVE_DISTANCE+(self.level-1)*MOVE_INCREMENT)
    def collisioncheck(self,player):
        for i in self.allcars:
            if(i.distance(player)<22):
                return True
        return False
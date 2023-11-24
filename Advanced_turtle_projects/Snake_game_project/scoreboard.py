from turtle import Turtle
import os.path

STYLE = ('Courier',12,'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        fileexists = os.path.exists('./Advanced_turtle_projects/Snake_game_project/highscore.txt')
        if(fileexists):
            with open('./Advanced_turtle_projects/Snake_game_project/highscore.txt') as f:
                self.highscore = int(f.readline().rstrip('\n'))
        else:
            self.highscore = 0
        self.score = 0
        self.hideturtle()
        self.pencolor('white')
        self.pu()
        self.goto(0,270)
        self.refresh()
    def oncollide(self):
        self.score += 1
        self.refresh()
    def refresh(self):
        self.clear()
        self.write(arg='Score: {} High score: {}'.format(self.score,self.highscore),align=ALIGNMENT,font=STYLE)
    def gamereset(self):
        if(self.score>int(self.highscore)):
            self.highscore = self.score
            with open('./Advanced_turtle_projects/Snake_game_project/highscore.txt','w') as f:
                f.write(str(self.highscore))
        self.score = 0
        self.reset()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0,270)
        self.refresh()
        # self.pu()
        # self.goto(0,0)
        # self.pd()
        # self.write(arg='GAME OVER',align=ALIGNMENT,font=("Courier",14,'bold'))
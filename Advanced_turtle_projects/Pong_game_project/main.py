from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time


def selectLevel():
    global no
    no = screen.numinput("Level","Enter level",-1,0,18)
    if(no!=-1):
        return True
    return False

def wantToContinue():
    t = screen.textinput("Play Again","Do you want to play again?")
    if(t.lower()=='yes' or t.lower()=='y'):
        return True
    return False

def keypress():
    screen.listen()
    screen.onkeypress(r_paddle.up,'Up')
    screen.onkeypress(r_paddle.down,'Down')
    screen.onkeypress(l_paddle.up,'w')
    screen.onkeypress(l_paddle.down,'s')

def initialise():
    global r_paddle,l_paddle,r_scoreboard,l_scoreboard,ball,line
    

    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350,0))

    r_scoreboard = Scoreboard((30,250))
    l_scoreboard = Scoreboard((-30,250))

    ball = Ball()
    ball.createBall()
    line = Line()

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
initialise()


isselected = selectLevel()

keypress()

game_on = True
x,y=10,10

while(game_on and isselected):
    screen.update()
    ball.move(x,y)

    if(l_scoreboard.checkwin()):
        game_on = False
        screen.reset()
        l_scoreboard.refreshwin(1)

        if(wantToContinue()):
            isselected = selectLevel()
            game_on = True
            initialise()
            l_scoreboard.no = 0
            r_scoreboard.no = 0
            r_scoreboard.update()
            l_scoreboard.update()
            keypress()
        else:
            isselected = False
            break

    elif(r_scoreboard.checkwin()):
        game_on = False
        screen.reset()
        r_scoreboard.refreshwin(2)

        if(wantToContinue()):
            isselected = selectLevel()
            game_on = True
            initialise()
            l_scoreboard.no = 0
            r_scoreboard.no = 0
            r_scoreboard.update()
            l_scoreboard.update()
            keypress()
        else:
            isselected = False
            break

    if(ball.rightwallbounce()):
        y*=-1
    elif(ball.leftwallbounce()):
        y*=-1

    if(r_paddle.collisionwithball(ball) or l_paddle.collisionwithball(ball)):
        x*=-1

    if(ball.rightoutofbounds()):
        l_scoreboard.no += 1
        l_scoreboard.update()
        ball.reset()
        ball.createBall()
    elif(ball.leftoutofbounds()):
        r_scoreboard.no += 1
        r_scoreboard.update()
        ball.reset()
        ball.createBall()
    time.sleep(0.04-0.0022*no)

if(isselected==False):
    screen.bye()
else:
    screen.exitonclick()
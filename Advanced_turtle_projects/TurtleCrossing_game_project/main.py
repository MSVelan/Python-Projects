import time,random
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move,"Up")
gameOn = True

car_manager = CarManager()
scoreboard = Scoreboard()

while(gameOn):
    screen.update()
    time.sleep(0.1)
    car_manager.createcar()
    car_manager.movecars()
    if(car_manager.collisioncheck(player)):
        gameOn = False
        screen.update()
        scoreboard.gameover()
    if(player.checkfinish()):
        car_manager.level += 1
        scoreboard.refresh(car_manager.level)
screen.exitonclick()
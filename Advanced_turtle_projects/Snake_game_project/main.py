from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.oncollide()

    if(snake.collisionWithWall()):
        snake.gamereset()
        scoreboard.gamereset()

    #Detecting collision with own tail or segment of snake
    for seg in snake.segments[1:]:
        if(snake.head.distance(seg)<10):
            snake.gamereset()
            scoreboard.gamereset()
screen.exitonclick()
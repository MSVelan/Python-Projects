import turtle as tur,random

screen = tur.Screen()
screen.setup(width=500,height=400)
colors = ['red','violet','indigo','blue','green','yellow','orange']
isRaceOn = False
turtle_list = []
for i in range(-3,4):
    t = tur.Turtle(shape="turtle")
    t.pu()
    t.color(colors[i+3])
    t.goto(-230,(i+0.5)*45-20)
    turtle_list.append(t)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color: ")
if(user_bet):
    isRaceOn = True

color_won = None

while(isRaceOn):
    rand_dist = random.randint(0,10)
    rand_turtle = random.choice(turtle_list)
    rand_turtle.forward(rand_dist)
    if(rand_turtle.xcor()>=230):
        isRaceOn = False
        color_won = rand_turtle.pencolor()

if(color_won == user_bet):
    print("You won.. {} won the race".format(color_won))
else:
    print("Better luck next time.. your guess was wrong, {} won the race".format(color_won))
screen.exitonclick()
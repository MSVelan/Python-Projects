import pandas
from turtle import Screen,shape
from showtext import Showtext
from scoreboard import Scoreboard
screen = Screen()
screen.title("Indian States Guessing Game")

image = "./blankmap.gif"
screen.addshape(image)
shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


data = pandas.read_csv("indian_states_pandas.csv")
scoreboard = Scoreboard()
answeredStates = []
screen.tracer(0)
gameOn = True
while(gameOn):
    answer = screen.textinput("Guess the state","What's another state name?")
    answer = answer.lower()
    if(answer == 'exit'):
        l = []
        for i in data['state']:
            if(i not in answeredStates):
                l.append(i)

        data_dict = {"Missed States":l}
        df = pandas.DataFrame(data_dict)
        df.to_csv("Missed_states_op.csv")
        break
    screen.update()
    for i in data['state']:
        if(answer == i.lower()):
            x = int(data[data['state'].str.lower() == answer].x)
            y = int(data[data['state'].str.lower() == answer].y)
            t = Showtext(i,(x,y))
            answeredStates.append(i)
            scoreboard.score += 1
            scoreboard.refresh()
            screen.update()
            break
    if(len(answeredStates) == 29):
        scoreboard.onwin()
        screen.update()

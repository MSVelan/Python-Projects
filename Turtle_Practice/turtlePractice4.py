import turtle as tur,random
tur.colormode(255)

t = tur.Turtle()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

t.speed("fastest")
for _ in range(int(360/5)):
    t.pencolor(random_color())
    t.circle(100)
    cur_heading = t.heading()
    t.setheading(cur_heading+5)

screen = tur.Screen()
screen.exitonclick()
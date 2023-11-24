
# Hirst spot painting

# import colorgram
# colors = colorgram.extract('sampleforturtlepractice5.jpg',90)
# color_pallete = [(i.rgb.r,i.rgb.g,i.rgb.b) for i in colors]

import random, turtle as tur


color_pallete = [(252, 244, 249), (242, 249, 252), (237, 230, 96), (13, 115, 170), (166, 79, 46), (188, 12, 63), (213, 157, 87), (129, 181, 203), (234, 76, 46), (33, 139, 83), (5, 34, 91), (146, 167, 35), (76, 40, 21), (110, 187, 165), (167, 47, 91), (227, 117, 147), (14, 170, 212), (59, 160, 89), (6, 95, 51), (219, 71, 119), (95, 21, 69), (240, 162, 190), (147, 205, 224), (12, 87, 106), (211, 222, 10), (248, 170, 145), (9, 45, 127), (7, 75, 41), (161, 210, 187), (137, 34, 27), (162, 190, 225), (104, 119, 165), (89, 61, 34)]

t = tur.Turtle()
screen = tur.Screen()
screen.colormode(255)
t.pu()
t.hideturtle()
t.goto(-250,-200)
t.speed(0)

for i in range(10):
    for j in range(10):
        color = color_pallete[random.randint(0,len(color_pallete)-1)]
        t.dot(20,int(color[0]),int(color[1]),int(color[2]))
        t.forward(50)
    y = t.position()[1]
    t.goto(-250,y+50)

screen.exitonclick()
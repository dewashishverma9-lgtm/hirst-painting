# import colorgram
from turtle import Turtle, Screen
import random

tut = Turtle()
Screen().colormode(255)


# colors = colorgram.extract('image.JPG',30)
# colour_list = []
# for color in colors:
#     rgb = color.rgb
#     colour_list.append((rgb.r, rgb.g,rgb.b))
colour_list = [(240, 242, 246), (240, 236, 229), (244, 239, 243), (236, 243, 239), (193, 160, 123), (73, 92, 124), (141, 87, 60), (142, 160, 186), (216, 209, 122), (183, 147, 163), (30, 33, 47), (56, 34, 25), (176, 160, 43), (121, 75, 93), (140, 174, 152), (79, 115, 81), (64, 29, 39), (136, 28, 19), (181, 102, 87), (118, 29, 41), (49, 58, 92), (103, 120, 167), (172, 101, 116), (31, 48, 43), (102, 155, 89), (217, 180, 174), (213, 177, 191), (179, 187, 211), (66, 81, 30), (165, 208, 188)]
tut.penup()
tut.right(180)
tut.forward(200)
tut.right(180)
tut.right(90)
tut.forward(200)
tut.left(90)

for _ in range(5):
    for _ in range(9):
        tut.dot(20)
        tut.pencolor(random.choice(colour_list))
        tut.penup()
        tut.forward(50)
    tut.left(90)
    tut.forward(50)
    tut.left(90)
    for _ in range(9):
        tut.dot(20)
        tut.pencolor(random.choice(colour_list))
        tut.penup()
        tut.forward(50)
    tut.right(90)
    tut.forward(50)
    tut.right(90)






Screen().exitonclick()

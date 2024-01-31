# import colorgram
#
# colors = colorgram.extract("download.jpeg", 10)
#
# colors_list = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.g
#     new = (r,g,b)
#     colors_list.append(new)
#
# print(colors_list)

from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
colors_list = [(194, 171, 171), (157, 99, 99), (124, 36, 36), (185, 159, 159), (7, 52, 52), (54, 29, 29)]
t = Turtle()
t.speed("fastest")
t.shape("arrow")


def random_color():
    return random.choice(colors_list)


def paint():
    for i in range(0, 501, 50):
        t.penup()
        t.sety(i)
        t.setx(0)
        for _ in range(10):
            t.dot(20, random_color())
            t.forward(50)


paint()
screen = Screen()
screen.exitonclick()

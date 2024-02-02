from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
height = -150
turtle_list = []
race_is_on = False
bet = screen.textinput(title="Make your bet", prompt="What color turtle do you want to bet")

if bet:
    race_is_on = True

for x in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[x])
    t.setx(-225)
    t.sety(height)
    height += 60
    turtle_list.append(t)

while race_is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_is_on = False
            if bet == winning_color:
                print("You've won!")
            else:
                print("You lost :(")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

from turtle import Turtle, Screen

t = Turtle()
s = Screen()



def forward():
    t.forward(20.0)


def backward():
    heading = t.heading()
    t.setheading(heading + 180)
    t.fd(20)


def right():
    heading = t.heading() - 10
    t.setheading(heading)


def left():
    heading = t.heading() + 10
    t.setheading(heading)


s.listen()
s.onkey(key="s", fun=backward)
s.onkey(key="w", fun=forward)
s.onkey(key="a", fun=left)
s.onkey(key="d", fun=right)
s.exitonclick()

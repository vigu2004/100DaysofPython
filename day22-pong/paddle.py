from turtle import Turtle

PADDLE_START = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(PADDLE_START[x])

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create()
        self.head = self.segment[0]

    def create(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segment.append(t)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for segment_no in range(len(self.segment) - 1, 0, -1):
            x = self.segment[segment_no - 1].xcor()
            y = self.segment[segment_no - 1].ycor()
            self.segment[segment_no].goto(x, y)
        self.segment[0].forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def reset(self):
        for segment in self.segment:
            segment.goto(1000,1000)
        self.segment.clear()
        self.create()
        self.head = self.segment[0]
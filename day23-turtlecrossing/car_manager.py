from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(random.randint(310,350),random.randint(-280,280))
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.color(random.choice(COLORS))

    def move_forward(self):
        while self.xcor() > -300 :
            self.forward(STARTING_MOVE_DISTANCE)


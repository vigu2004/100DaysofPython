from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.car_list = []
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1,stretch_len=3)
        car.penup()
        car.color(random.choice(COLORS))
        y_cor = random.randint(-270,270)
        car.goto(300,y_cor)
        self.car_list.append(car)

    def move_car(self):
        for x in self.car_list:
            x.backward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT
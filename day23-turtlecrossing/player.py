from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.reset_game()


    def move_forward(self):
            self.forward(MOVE_DISTANCE)



    def reset_game(self):
        self.goto(x=0,y=-280)

    def game_end(self):
        return self.ycor() > 280


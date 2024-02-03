from turtle import Turtle, Screen
import random
import time
from snake import Snake


screen = Screen()
screen.bgcolor("black")
screen.title("Snake :)")
screen.setup(height=600, width=600)
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.right , "Right")
screen.onkey(snake.left , "Left")


game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()

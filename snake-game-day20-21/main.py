from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.title("Snake :)")
screen.setup(height=600, width=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
game_over = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

p_right = Paddle(0)
p_left = Paddle(1)
b = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(fun=p_right.up, key="Up")
screen.onkey(fun=p_right.down, key="Down")

screen.onkey(fun=p_left.up, key="w")
screen.onkey(fun=p_left.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(b.move_speed)
    b.move()

    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_wall()

    if p_right.distance(b) < 50 and b.xcor() > 320 or p_left.distance(b) < 50 and b.xcor() < -320:
        b.bounce_paddle()

    if b.xcor() > 380:
        b.reset_position()
        score.l_point()
        score.update_score()

    if b.xcor() < -380:
        b.reset_position()
        score.r_point()
        score.update_score()

screen.exitonclick()

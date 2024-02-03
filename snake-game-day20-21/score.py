from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.current_score}", move=False, align="center", font=('comic sans', 10, 'normal'))

    def game_over(self):
        self.goto(-170, -50)
        self.write(arg="Game Over!", move=False, font=('comic sans', 50, 'normal'))

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()


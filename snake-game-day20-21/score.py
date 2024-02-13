from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.high_score = 0
    def update_scoreboard(self):
        self.clear()
        with open(file="data.txt") as f:
            self.high_score = f.read()

        self.write(arg=f"Score: {self.current_score} , Highscore: {self.high_score}", move=False, align="center", font=('comic sans', 10, 'normal'))

    # def game_over(self):
    #     self.goto(-170, -50)
    #     self.write(arg="Game Over!", move=False, font=('comic sans', 50, 'normal'))


    def reset(self):
        if int(self.high_score) < self.current_score:
            self.high_score = self.current_score
            self.high_score = str(self.high_score)
            with open(file="data.txt" , mode="w") as f:
                f.write(self.high_score)

        self.current_score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()


score = Score()
print(score.high_score)
import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("USA")

img ="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
states = data.state.to_list()
guessed = []


right = 0

while right <= 50:
    answer = str(screen.textinput(title=f"{right}/50 Guessed" , prompt="Enter your next state"))
    answer = answer.title()

    if answer == "Exit":
        break

    if answer in states:
        answer_row = data[data["state"] == answer]
        guessed.append(answer)
        text_screen = turtle.Turtle()
        text_screen.penup()
        text_screen.hideturtle()
        text_screen.goto(int(answer_row.x),int(answer_row.y))
        text_screen.write(arg=f"{answer}")
        right += 1


states_to_learn = []
for state in states:
    if state not in guessed:
        states_to_learn.append(state)


x = pd.DataFrame(states_to_learn)
x.to_csv("States_To_Learn.csv")

screen.exitonclick()
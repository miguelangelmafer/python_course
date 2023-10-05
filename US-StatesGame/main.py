import turtle
from turtle import Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
correct_answer = []

while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(correct_answer)} / 50",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_answer]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        if answer_state not in correct_answer:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(answer_state)
            correct_answer.append(answer_state)

screen.exitonclick()

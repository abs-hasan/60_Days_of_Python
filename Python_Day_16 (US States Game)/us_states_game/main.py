import turtle
from turtle import Turtle, Screen

import pandas
import pandas as pd

IMAGE_LINK = "Image/blank_states_img.gif"
# COORDINATOR_FILE =

screen = Screen()
screen.setup()
screen.title("U.S States Game")

# with open("Data/50_states.csv")
screen.addshape(IMAGE_LINK)
turtle.shape(IMAGE_LINK)

data = pd.read_csv("Data/50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        t.goto(x_cor, y_cor)
        t.write(state_data.state.item())


# states to learn.csv
# if guessed_states in


# def get_click_cor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_click_cor)
# turtle.mainloop()

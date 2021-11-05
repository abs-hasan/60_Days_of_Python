from turtle import Turtle, Screen
import random


color = ["red", 'green', 'blue', 'purple', 'orange', 'grey']
x_corr = -220
y_corr = 150

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

all_turtles = []

for value in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[value])
    new_turtle.goto(x= x_corr, y=-y_corr)
    y_corr -=60
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


# import turtle
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


screen.exitonclick()

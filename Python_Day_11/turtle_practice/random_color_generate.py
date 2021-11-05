import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t = (r, g, b)
    return t


tim.pensize(15)
tim.speed(50)
turtle.colormode(255)

for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))



tim_s = Screen()
tim_s.exitonclick()

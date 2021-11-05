import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = Turtle()
tim.speed(0)
turtle.colormode(255)


def draw_spirograph(size_of_graph):
    for _ in range(int(360/ size_of_graph)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading()+size_of_graph)

draw_spirograph(1)


tim_s = Screen()
tim_s.exitonclick()

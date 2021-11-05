import turtle
from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []

image = "./Image/spot_painting.jpg"
colors = colorgram.extract(image, 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)
tim = Turtle()
tim.hideturtle()
turtle.colormode(255)
tim.speed(0)

tim.setheading(225)
tim.penup()

tim.forward(300)
tim.setheading(0)
number_of_dots = 3601

for dot_count in range(1, number_of_dots):
    tim.dot(10, random.choice(rgb_colors))
    tim.forward(10)

    if dot_count % 60 == 0:
        tim.setheading(90)
        tim.forward(10)
        tim.setheading(180)
        tim.forward(600)
        tim.setheading(0)



tim_s = Screen() # tim_s is object and Screen() is class and turtle is module
tim_s.exitonclick()

from turtle import Turtle, Screen
import random

tim = Turtle()

# todo shape
tim.shape("turtle")

# todo color: getting from pen color
tim.color("red")

# todo : draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Todo : Draw a dash line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Todo: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)


color = ["red",'green','blue','pink','purple','yellow','orange','grey']

for value in range(3,11):
    a_degree = 360 / value
    tim.pencolor(random.choice(color))
    for a in range(value):
        tim.forward(100)
        tim.right(a_degree)







tim = Screen()
tim.exitonclick()

# turtle.Screen()

# Turtle.getscreen()

# turtle.mainloop()
# turtle.exitonclick()

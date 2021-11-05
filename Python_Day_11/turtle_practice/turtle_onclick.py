import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def clock_wise():
    tim.right(5)


def anti_clock():
    tim.left(5)


def back():
    tim.backward(5)

def cs():
    tim.clear()
    tim.penup()
    tim.speed(0)
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=anti_clock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=cs)



screen.exitonclick()
import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

turtle.speed("fastest")
turtle.pensize(3)
for _ in range(320):
    turtle.color(random_color())
    turtle.circle(120)
    turtle.left(10)

screen.exitonclick()

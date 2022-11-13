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
def draw_spirograph(spaces):
    #dividing 360 by spaces because a circle has 360 degrees, and spaces determines the number of spaces between the circles of the spirograph
    #if they are 4, then 360/4 will = 90, which means there will be 90 circles, hence making it loop for as long as necessary
    for _ in range(int(360 / spaces)):
        turtle.color(random_color())
        turtle.circle(120)
        turtle.setheading(turtle.heading() + spaces)

draw_spirograph(4)
screen.exitonclick()

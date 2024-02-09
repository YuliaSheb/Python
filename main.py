import random
import turtle
from turtle import Turtle, Screen


def conner(grad):
    conn = 360/grad
    return conn


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    collor = (r, g, b)
    return collor


def draw_circle():
    for i in range(10):
        for j in range(10):
            tinny_turtle.color(random_color())
            tinny_turtle.dot(20)
            tinny_turtle.color("white")
            tinny_turtle.forward(50)
        tinny_turtle.setheading(90)
        tinny_turtle.forward(50)
        tinny_turtle.setheading(180)
        tinny_turtle.forward(500)
        tinny_turtle.setheading(0)


turtle.colormode(255)
tinny_turtle = Turtle()
tinny_turtle.hideturtle()
tinny_turtle.setheading(225)
tinny_turtle.color("white")
tinny_turtle.forward(300)
tinny_turtle.setheading(0)
tinny_turtle.speed(0)
tinny_turtle.pensize(1)

draw_circle()

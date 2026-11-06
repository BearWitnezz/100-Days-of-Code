color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88),
                  (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99),
                  (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55),
                  (15, 96, 71), (33, 60, 106)]
import random
import turtle
from turtle import Turtle, Screen


def hirst(rows):
    """Paint a Hirst-style spot painting with the given number of rows."""
    turtle.colormode(255)
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    y = -255
    tim.teleport(-255, y)
    for _ in range(rows):
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
        y += 50
        tim.teleport(-255, y)
    tim.ht()


hirst(10)

screen = Screen()
screen.exitonclick()

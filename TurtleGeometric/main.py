from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy_the_turtle.color(R, G, B)


for i in range(3, 11):
    for _ in range(i):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360 / i)
        timmy_the_turtle.forward(100)
    change_color()

screen = Screen()
screen.exitonclick()

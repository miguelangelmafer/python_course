from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed("fastest")


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    timmy_the_turtle.pencolor(r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        change_color()


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

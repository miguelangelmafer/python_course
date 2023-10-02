from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("normal")


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    timmy_the_turtle.pencolor(r, g, b)


directions = [0, 90, 180, 270]

for _ in range(100):
    timmy_the_turtle.forward(40)
    timmy_the_turtle.setheading(random.choice(directions))
    change_color()

screen = Screen()
screen.exitonclick()

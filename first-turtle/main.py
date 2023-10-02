from turtle import Turtle, Screen


def make_square():
    timmy.color("blue")
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
make_square()

my_screen = Screen()
my_screen.exitonclick()
print(my_screen)

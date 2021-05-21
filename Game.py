import turtle
import sys
sys.setrecursionlimit(2147483647)
background = turtle.Screen()
background.title("Snake Game")
background.bgcolor("light grey")
print(background.screensize())
root = turtle.Turtle()
root.shape("turtle")
root.color("teal")


def turnright():
    root.setheading(0)
    root.forward(10)


def turnleft():
    root.setheading(180)
    root.forward(10)


def turnupward():
    root.setheading(90)
    root.forward(10)


def turndownward():
    root.setheading(-90)
    root.forward(10)


def jumpup():
    root.setheading(90)
    root.forward(50)
    root.backward(30)
    jumpup()


turtle.onkeypress(turnright, "d")
turtle.onkeypress(turnleft, "a")
turtle.onkeypress(turnupward, "w")
turtle.onkeypress(turndownward, "s")
turtle.onkeypress(jumpup, "space")
turtle.listen()
turtle.done()

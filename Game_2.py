import turtle
import sys
import random
score = 0
prevscore = 0
sys.setrecursionlimit(2147483647)
background = turtle.Screen()
background.title("Snake Game")
background.bgcolor("light grey")
print(background.screensize())
root = turtle.Turtle()
root.shape("square")
root.color("teal")
root.direction = "Stop"
root.penup()
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, -200)
segment = turtle.Turtle()
segment.shape("square")
segment.color("blue")
segment.penup()
body = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("teal")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score : 0", align="center", font=("Times New Roman", 24, "bold"))


def rightturn():
    root.right(90)
    turtle.update()


def leftturn():
    root.left(90)
    turtle.update()


turtle.listen()
while True:
    root.forward(5)
    turtle.onkeypress(rightturn, "d")
    turtle.onkeypress(leftturn, "a")
    if root.xcor() > 330 or root.xcor() < -330:
        exit()
    if root.ycor() > 330 or root.ycor() < -330:
        exit()
    root.forward(5)
    foodtouch = root.distance(food)
    if foodtouch < 20:
        score = score + 1
        print(score)
        food.hideturtle()
        food.setposition(random.randint(-300, 300), random.randint(-300, 300))
        food.showturtle()
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        body.append(new_segment)
    for index in range(len(body)-1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].setposition(x, y)
    if len(body) > 0:
        x = root.xcor()
        y = root.ycor()
        body[0].setposition(x, y)
    if score != prevscore:
        pen.clear()
    prevscore = score
    pen.color("blue")
    pen.write("Score : {}".format(score), align="center", font=("Times New Roman", 24, "bold"))

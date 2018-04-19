# Random stuff

import turtle
import random

t = turtle.Turtle()
t.screen.bgcolor("black")
t.speed(200)


def random_drawing(turns):

    for x in range(turns):
        right = t.right(random.randint(0, 360))
        left = t.left(random.randint(0, 360))
        t.color(random.choice(["blue", "red", "green", "orange", "white"]))
        random.choice([right, left])
        t.forward(random.randint(1, 30))


random_drawing(500)

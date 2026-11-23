
import turtle

import random

t = turtle.Turtle()


for i in range(20):
    t.pencolor(random.choice(["hotpink","cyan","yellow"]))
    t.forward(i*5)
    t.right(30)

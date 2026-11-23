import turtle
import random

wn = turtle.Screen()

t = turtle.Turtle() 

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

colors = ["red", "blue", "green", "yellow", "black"]

# Does not work properly.
def clickLeft(x, y):  # Make sure to have parameters x, y
    t.color(random.choice(colors))

def clickRight(x, y):
    t.stamp()

wn.listen()

wn.onclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
wn.onclick(clickRight, 3) # 3: Right Mouse Button

wn.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")

# tim.mainloop()  # This will make sure the program continues to run 

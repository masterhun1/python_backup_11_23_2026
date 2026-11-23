
"""

Trinket: "Have a Happy Emoji Xmas!"
Link: https://trinket.io/python/b9497c1124

Get emojies at ... 
Link: https://emojipedia.org/christmas-tree/


"""


import turtle, random

def moveTo(pen, x_cor, y_cor):
  pen.penup()
  pen.goto(x_cor, y_cor)
  pen.pendown()


# This line creates the screen object.
screen = turtle.Screen()

# Background color
screen.bgcolor("red")

# This line creates the turtle object.
hh = turtle.Turtle()

# Speed settings
# 0 is the fastest.
# 1 is the slowest.
# 6 or 7 is average speed.
hh.speed(2)

hh.hideturtle()

moveTo(hh, -165, 90)

hh.color("white")

# For the font, "Times" or "Arial"
# For style, "italic" or "bold" or "normal"
hh.write("Seasons Greetings", move=False, align="left", font=("Times", 32, "bold"))

moveTo(hh, -150, -50)

hh.write("🎄⛄🎄", move = False, align="left", font=("Times", 62, "bold"))

# This is the botton messages.

moveTo(hh, -155, 40)

hh.color("white")

# "normal" or "bold" or "italic"
# "Times" or "Arial" or "Comic Sans MS"
hh.write("🎅Happy Holidays🤑", move=False, align="left", font=("Times", 24, "bold"))

moveTo(hh, -150, -95)

hh.color("white")

hh.write("👍️From Master Hun💻🥋", move=False, align="left", font=("Times", 14, "normal"))

# Snow generator
hh.speed(7)

hh.hideturtle()

# Keeps the window open.
turtle.done()

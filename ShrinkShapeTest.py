import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=600, height=400)

# Create a turtle
t = turtle.Turtle()
t.speed(1) # Slow for demonstration

# Draw a large square
t.pensize(3)
t.color("blue")
for _ in range(4):
    t.forward(100)
    t.right(90)

# Shrink the turtle's shape and draw a smaller square
t.shapesize(0.5, 0.5, 1) # Shrink to half size
t.penup()
t.goto(-100, -50) # Move to a new position
t.pendown()
t.color("red")
for _ in range(4):
    t.forward(100) # The actual drawn length will be scaled by shapesize
    t.right(90)

turtle.done()

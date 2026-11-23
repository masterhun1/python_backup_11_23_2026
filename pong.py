# Simple Pong in Python 3 for Beginners
# By @TokyoEdtech

import turtle

# 1. Setup the game window
wn = turtle.Screen()
wn.title("Pong by @TokyoEdtech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Stops the window from updating automatically (speeds up the game)

# Score tracking variables
score_a = 0
score_b = 0

# 2. Create Paddle A (Left Paddle)
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Animation speed (0 is the fastest possible)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretches the default 20x20 square
paddle_a.penup()  # Prevents drawing lines when moving
paddle_a.goto(-350, 0)

# 3. Create Paddle B (Right Paddle)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# 4. Create the Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ball movement speed along X axis (adjust if too fast/slow)
ball.dy = 0.2  # Ball movement speed along Y axis

# 5. Create the Pen (Scoreboard display)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  # Hide the actual pen arrow icon
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# 6. Functions for Paddle Movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# 7. Keyboard Binding Controls
wn.listen()  # Tells the program to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# 8. Main Game Loop
while True:
    wn.update()  # Update the screen on every loop cycle

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and Bottom Boundary Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverse direction

    # Left and Right Boundary Checking (Scoring)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # Reset ball and swap initial launch direction
        score_a += 1
        pen.clear()  # Erase the old score text
        pen.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Paddle and Ball Collisions
    # Right Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1

    # Left Paddle Collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1

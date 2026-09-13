# name = input("Enter your name: ")
# print(f"Hello, {name}!")
# name = "Abdur"
# print("Hello,", name)
# print("Welcome to Python!")



# Code 2: Turtle bouncing ball with gravity
import turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.goto(0, 100)
vx, vy = 3, 0
gravity = -0.5
while True:
    vy += gravity
    ball.goto(ball.xcor() + vx, ball.ycor() + vy)
    if ball.ycor() < -200:
        ball.sety(-200)
        vy = -vy * 0.8
    if ball.xcor() > 300 or ball.xcor() < -300:
        vx = -vx
    # time.sleep(0.02)
# Code 3: Turtle spiral animation (colorful)
import turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i * 2 / 3)
    t.left(59)
turtle.done()
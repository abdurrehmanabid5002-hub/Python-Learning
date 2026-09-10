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


# Code 1: Terminal loading spinner
import sys, time
spinner = ['|', '/', '-', '\\']
for i in range(50):
    sys.stdout.write(f'\rLoading {spinner[i % 4]}')
    sys.stdout.flush()
    time.sleep(0.1)
print('\nDone!')
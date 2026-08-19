import numpy as np 
import pandas as pd 
import tkinter as tk

# Create window
window = tk.Tk()
window.title("Animated Bouncing Ball")
window.geometry("800x500")
window.resizable(False, False)

# Create canvas
canvas = tk.Canvas(window, width=800, height=500, bg="black")
canvas.pack()

# Ball properties
x = 100
y = 100
radius = 30

dx = 5
dy = 4

# Create ball
ball = canvas.create_oval(
    x - radius,
    y - radius,
    x + radius,
    y + radius,
    fill="red",
    outline="white",
    width=2
)

def animate():
    global dx, dy

    # Move ball
    canvas.move(ball, dx, dy)

    # Get ball position
    left, top, right, bottom = canvas.coords(ball)

    # Bounce from left/right walls
    if left <= 0 or right >= 800:
        dx = -dx

    # Bounce from top/bottom walls
    if top <= 0 or bottom >= 500:
        dy = -dy

    # Run animation again after 10 milliseconds
    window.after(10, animate)


# Start animation
animate()

# Start Tkinter
window.mainloop()
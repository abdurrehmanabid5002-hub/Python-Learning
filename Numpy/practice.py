'''import numpy as np 
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
window.mainloop()'''

import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Try a higher number.")

        elif guess > number:
            print("Try a lower number.")

        else:
            print(f"You got it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a whole number.")


'''from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Animated GDP and population over decades'),
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=["GDP - Scatter", "Population - Bar"],
        value='GDP - Scatter',
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(
    Output("graph", "figure"),
    Input("selection", "value"))
def display_animated_graph(selection):
    df = px.data.gapminder() # replace with your own data source
    animations = {
        'GDP - Scatter': px.scatter(
            df, x="gdpPercap", y="lifeExp", animation_frame="year",
            animation_group="country", size="pop", color="continent",
            hover_name="country", log_x=True, size_max=55,
            range_x=[100,100000], range_y=[25,90]),
        'Population - Bar': px.bar(
            df, x="continent", y="pop", color="continent",
            animation_frame="year", animation_group="country",
            range_y=[0,4000000000]),
    }
    return animations[selection]


app.run(debug=True)'''
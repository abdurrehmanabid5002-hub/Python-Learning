import tkinter as tk
import random

# =========================
# GAME SETTINGS
# =========================
WIDTH = 700
HEIGHT = 500
CELL_SIZE = 20

INITIAL_SPEED = 120
MIN_SPEED = 55
SPEED_INCREASE = 2


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        # -------------------------
        # Top information panel
        # -------------------------
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(fill="x")

        self.score_label = tk.Label(
            self.info_frame,
            text="Score: 0",
            font=("Arial", 16, "bold")
        )
        self.score_label.pack(side="left", padx=15, pady=8)

        self.high_score_label = tk.Label(
            self.info_frame,
            text="High Score: 0",
            font=("Arial", 16, "bold")
        )
        self.high_score_label.pack(side="right", padx=15, pady=8)

        # -------------------------
        # Game canvas
        # -------------------------
        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg="#111111",
            highlightthickness=0
        )
        self.canvas.pack()

        # -------------------------
        # Controls
        # -------------------------
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))

        self.root.bind("<w>", lambda event: self.change_direction("Up"))
        self.root.bind("<s>", lambda event: self.change_direction("Down"))
        self.root.bind("<a>", lambda event: self.change_direction("Left"))
        self.root.bind("<d>", lambda event: self.change_direction("Right"))

        self.root.bind("<W>", lambda event: self.change_direction("Up"))
        self.root.bind("<S>", lambda event: self.change_direction("Down"))
        self.root.bind("<A>", lambda event: self.change_direction("Left"))
        self.root.bind("<D>", lambda event: self.change_direction("Right"))

        self.root.bind("<space>", lambda event: self.restart())

        self.high_score = 0

        self.restart()

    # =========================
    # START / RESTART GAME
    # =========================
    def restart(self):
        self.canvas.delete("all")

        self.snake = [
            (300, 240),
            (280, 240),
            (260, 240)
        ]

        self.direction = "Right"
        self.next_direction = "Right"

        self.score = 0
        self.speed = INITIAL_SPEED
        self.game_over = False

        self.score_label.config(text="Score: 0")
        self.high_score_label.config(
            text=f"High Score: {self.high_score}"
        )

        self.create_food()
        self.draw()

        self.root.after(self.speed, self.game_loop)

    # =========================
    # CHANGE DIRECTION
    # =========================
    def change_direction(self, new_direction):

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        # Prevent snake from reversing into itself
        if new_direction != opposite[self.direction]:
            self.next_direction = new_direction

    # =========================
    # CREATE FOOD
    # =========================
    def create_food(self):

        while True:
            x = random.randrange(
                0,
                WIDTH,
                CELL_SIZE
            )

            y = random.randrange(
                0,
                HEIGHT,
                CELL_SIZE
            )

            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    # =========================
    # GAME LOOP
    # =========================
    def game_loop(self):

        if self.game_over:
            return

        self.direction = self.next_direction

        head_x, head_y = self.snake[0]

        # Move snake
        if self.direction == "Up":
            head_y -= CELL_SIZE

        elif self.direction == "Down":
            head_y += CELL_SIZE

        elif self.direction == "Left":
            head_x -= CELL_SIZE

        elif self.direction == "Right":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # -------------------------
        # Collision with walls
        # -------------------------
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            self.end_game()
            return

        # -------------------------
        # Collision with itself
        # -------------------------
        if new_head in self.snake:
            self.end_game()
            return

        self.snake.insert(0, new_head)

        # -------------------------
        # Eat food
        # -------------------------
        if new_head == self.food:

            self.score += 10

            if self.score > self.high_score:
                self.high_score = self.score

            self.score_label.config(
                text=f"Score: {self.score}"
            )

            self.high_score_label.config(
                text=f"High Score: {self.high_score}"
            )

            # Increase speed
            self.speed = max(
                MIN_SPEED,
                self.speed - SPEED_INCREASE
            )

            self.create_food()

        else:
            # Remove tail
            self.snake.pop()

        self.draw()

        self.root.after(
            self.speed,
            self.game_loop
        )

    # =========================
    # DRAW GAME
    # =========================
    def draw(self):

        self.canvas.delete("all")

        # Draw food
        fx, fy = self.food

        self.canvas.create_oval(
            fx + 2,
            fy + 2,
            fx + CELL_SIZE - 2,
            fy + CELL_SIZE - 2,
            fill="red",
            outline=""
        )

        # Draw snake
        for index, (x, y) in enumerate(self.snake):

            if index == 0:
                # Snake head
                self.canvas.create_rectangle(
                    x + 1,
                    y + 1,
                    x + CELL_SIZE - 1,
                    y + CELL_SIZE - 1,
                    fill="#00ff66",
                    outline=""
                )

            else:
                # Snake body
                self.canvas.create_rectangle(
                    x + 2,
                    y + 2,
                    x + CELL_SIZE - 2,
                    y + CELL_SIZE - 2,
                    fill="#00aa44",
                    outline=""
                )

    # =========================
    # GAME OVER
    # =========================
    def end_game(self):

        self.game_over = True

        self.canvas.create_rectangle(
            150,
            150,
            550,
            350,
            fill="#222222",
            outline="white",
            width=2
        )

        self.canvas.create_text(
            WIDTH // 2,
            200,
            text="GAME OVER",
            fill="red",
            font=("Arial", 36, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            250,
            text=f"Score: {self.score}",
            fill="white",
            font=("Arial", 20, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            290,
            text="Press SPACE to restart",
            fill="white",
            font=("Arial", 14)
        )


# =========================
# RUN GAME
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
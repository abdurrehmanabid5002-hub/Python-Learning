import pygame
import random
from collections import deque
from dataclasses import dataclass


# ============================================================
# CONFIGURATION
# ============================================================

WIDTH = 900
HEIGHT = 700

CELL_SIZE = 25

GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

FPS = 60

START_SPEED = 9
MAX_SPEED = 18

WINDOW_TITLE = "Snake X - DSA Edition"


# ============================================================
# COLORS
# ============================================================

BACKGROUND = (18, 18, 24)
GRID_COLOR = (32, 32, 42)

SNAKE_HEAD = (80, 220, 120)
SNAKE_BODY = (45, 180, 95)

FOOD_COLOR = (245, 80, 85)

TEXT_COLOR = (240, 240, 245)
SECONDARY_TEXT = (150, 150, 165)

PAUSE_COLOR = (255, 190, 60)


# ============================================================
# DIRECTIONS
# ============================================================

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


OPPOSITE_DIRECTION = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}


# ============================================================
# GAME DATA
# ============================================================

@dataclass
class GameStats:
    score: int = 0
    high_score: int = 0
    level: int = 1


# ============================================================
# SNAKE CLASS
# ============================================================

class Snake:
    """
    Snake implementation using:

    deque:
        Efficient O(1) insertion/removal from both ends.

    set:
        O(1) average-time collision checking.
    """

    def __init__(self):
        center_x = GRID_WIDTH // 2
        center_y = GRID_HEIGHT // 2

        self.body = deque([
            (center_x, center_y),
            (center_x - 1, center_y),
            (center_x - 2, center_y)
        ])

        # Used for O(1) collision detection
        self.occupied = set(self.body)

        self.direction = RIGHT
        self.next_direction = RIGHT

        self.growing = False

    @property
    def head(self):
        return self.body[0]

    def change_direction(self, new_direction):
        """
        Prevent the snake from instantly reversing.
        """

        if new_direction == OPPOSITE_DIRECTION[self.direction]:
            return

        self.next_direction = new_direction

    def move(self):
        """
        Move snake by one grid cell.
        """

        self.direction = self.next_direction

        head_x, head_y = self.head
        direction_x, direction_y = self.direction

        new_head = (
            head_x + direction_x,
            head_y + direction_y
        )

        self.body.appendleft(new_head)
        self.occupied.add(new_head)

        if not self.growing:
            tail = self.body.pop()
            self.occupied.remove(tail)

        self.growing = False

    def grow(self):
        """
        Make the snake one segment longer.
        """

        self.growing = True

    def hits_wall(self):
        x, y = self.head

        return (
            x < 0 or
            x >= GRID_WIDTH or
            y < 0 or
            y >= GRID_HEIGHT
        )

    def hits_self(self):
        """
        Check whether the head collides with the body.

        Using a set makes this approximately O(1).
        """

        head = self.head

        # Ignore the head itself
        body_without_head = self.occupied.copy()
        body_without_head.discard(head)

        return head in body_without_head

    def reset(self):
        self.__init__()


# ============================================================
# FOOD CLASS
# ============================================================

class Food:

    def __init__(self):
        self.position = None
        self.spawn(set())

    def spawn(self, occupied_cells):
        """
        Generate food at a position not occupied by the snake.
        """

        available_cells = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in occupied_cells
        ]

        if available_cells:
            self.position = random.choice(available_cells)

    def respawn(self, snake):
        self.spawn(snake.occupied)


# ============================================================
# GAME CLASS
# ============================================================

class SnakeGame:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        # Fonts
        self.title_font = pygame.font.SysFont(
            "arial",
            34,
            bold=True
        )

        self.score_font = pygame.font.SysFont(
            "arial",
            24,
            bold=True
        )

        self.small_font = pygame.font.SysFont(
            "arial",
            18
        )

        self.large_font = pygame.font.SysFont(
            "arial",
            52,
            bold=True
        )

        # Game objects
        self.snake = Snake()
        self.food = Food()

        self.stats = GameStats()

        self.running = True
        self.paused = False
        self.game_over = False

        self.speed = START_SPEED

        # Movement timer
        self.move_timer = 0

    # --------------------------------------------------------
    # RESET GAME
    # --------------------------------------------------------

    def restart(self):

        self.snake.reset()

        self.food.respawn(self.snake)

        self.stats.score = 0
        self.stats.level = 1

        self.speed = START_SPEED

        self.paused = False
        self.game_over = False

        self.move_timer = 0

    # --------------------------------------------------------
    # HANDLE INPUT
    # --------------------------------------------------------

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_UP, pygame.K_w):
                    self.snake.change_direction(UP)

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.snake.change_direction(DOWN)

                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.snake.change_direction(LEFT)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.snake.change_direction(RIGHT)

                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused

                elif event.key == pygame.K_r:
                    self.restart()

                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    # --------------------------------------------------------
    # UPDATE GAME
    # --------------------------------------------------------

    def update(self, delta_time):

        if self.paused or self.game_over:
            return

        self.move_timer += delta_time

        movement_interval = 1000 / self.speed

        if self.move_timer >= movement_interval:

            self.move_timer = 0

            self.snake.move()

            # Wall collision
            if self.snake.hits_wall():
                self.end_game()
                return

            # Self collision
            if self.snake.hits_self():
                self.end_game()
                return

            # Food collision
            if self.snake.head == self.food.position:

                self.snake.grow()

                self.stats.score += 10

                self.food.respawn(self.snake)

                self.update_level()

    # --------------------------------------------------------
    # LEVEL SYSTEM
    # --------------------------------------------------------

    def update_level(self):

        # Every 50 points -> new level
        self.stats.level = self.stats.score // 50 + 1

        self.speed = min(
            START_SPEED + (self.stats.level - 1) * 1.5,
            MAX_SPEED
        )

    # --------------------------------------------------------
    # GAME OVER
    # --------------------------------------------------------

    def end_game(self):

        self.game_over = True

        if self.stats.score > self.stats.high_score:

            self.stats.high_score = self.stats.score

    # --------------------------------------------------------
    # DRAW GRID
    # --------------------------------------------------------

    def draw_grid(self):

        for x in range(0, WIDTH, CELL_SIZE):

            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (x, 0),
                (x, HEIGHT)
            )

        for y in range(0, HEIGHT, CELL_SIZE):

            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (0, y),
                (WIDTH, y)
            )

    # --------------------------------------------------------
    # DRAW SNAKE
    # --------------------------------------------------------

    def draw_snake(self):

        for index, (x, y) in enumerate(self.snake.body):

            rectangle = pygame.Rect(
                x * CELL_SIZE + 2,
                y * CELL_SIZE + 2,
                CELL_SIZE - 4,
                CELL_SIZE - 4
            )

            if index == 0:

                pygame.draw.rect(
                    self.screen,
                    SNAKE_HEAD,
                    rectangle,
                    border_radius=7
                )

                # Eyes
                self.draw_eyes(rectangle)

            else:

                pygame.draw.rect(
                    self.screen,
                    SNAKE_BODY,
                    rectangle,
                    border_radius=6
                )

    # --------------------------------------------------------
    # DRAW SNAKE EYES
    # --------------------------------------------------------

    def draw_eyes(self, rectangle):

        eye_size = 4

        if self.snake.direction == RIGHT:

            eyes = [
                (rectangle.right - 8, rectangle.top + 6),
                (rectangle.right - 8, rectangle.bottom - 6)
            ]

        elif self.snake.direction == LEFT:

            eyes = [
                (rectangle.left + 8, rectangle.top + 6),
                (rectangle.left + 8, rectangle.bottom - 6)
            ]

        elif self.snake.direction == UP:

            eyes = [
                (rectangle.left + 6, rectangle.top + 8),
                (rectangle.right - 6, rectangle.top + 8)
            ]

        else:

            eyes = [
                (rectangle.left + 6, rectangle.bottom - 8),
                (rectangle.right - 6, rectangle.bottom - 8)
            ]

        for eye in eyes:

            pygame.draw.circle(
                self.screen,
                BACKGROUND,
                eye,
                eye_size
            )

    # --------------------------------------------------------
    # DRAW FOOD
    # --------------------------------------------------------

    def draw_food(self):

        if self.food.position is None:
            return

        x, y = self.food.position

        center = (
            x * CELL_SIZE + CELL_SIZE // 2,
            y * CELL_SIZE + CELL_SIZE // 2
        )

        pygame.draw.circle(
            self.screen,
            FOOD_COLOR,
            center,
            CELL_SIZE // 2 - 4
        )

        # Small highlight
        pygame.draw.circle(
            self.screen,
            (255, 150, 150),
            (
                center[0] - 4,
                center[1] - 4
            ),
            3
        )

    # --------------------------------------------------------
    # DRAW UI
    # --------------------------------------------------------

    def draw_ui(self):

        title = self.title_font.render(
            "SNAKE X",
            True,
            TEXT_COLOR
        )

        score = self.score_font.render(
            f"Score: {self.stats.score}",
            True,
            TEXT_COLOR
        )

        high_score = self.score_font.render(
            f"Best: {self.stats.high_score}",
            True,
            TEXT_COLOR
        )

        level = self.score_font.render(
            f"Level: {self.stats.level}",
            True,
            TEXT_COLOR
        )

        controls = self.small_font.render(
            "WASD / Arrow Keys   •   SPACE: Pause   •   R: Restart   •   ESC: Quit",
            True,
            SECONDARY_TEXT
        )

        self.screen.blit(
            title,
            (20, 12)
        )

        self.screen.blit(
            score,
            (220, 18)
        )

        self.screen.blit(
            high_score,
            (390, 18)
        )

        self.screen.blit(
            level,
            (560, 18)
        )

        self.screen.blit(
            controls,
            (
                20,
                HEIGHT - 30
            )
        )

    # --------------------------------------------------------
    # OVERLAY
    # --------------------------------------------------------

    def draw_overlay(self):

        if self.paused:

            overlay = pygame.Surface(
                (WIDTH, HEIGHT),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 130)
            )

            self.screen.blit(
                overlay,
                (0, 0)
            )

            text = self.large_font.render(
                "PAUSED",
                True,
                PAUSE_COLOR
            )

            instruction = self.small_font.render(
                "Press SPACE to continue",
                True,
                TEXT_COLOR
            )

            self.screen.blit(
                text,
                text.get_rect(
                    center=(WIDTH // 2, HEIGHT // 2 - 20)
                )
            )

            self.screen.blit(
                instruction,
                instruction.get_rect(
                    center=(WIDTH // 2, HEIGHT // 2 + 35)
                )
            )

        elif self.game_over:

            overlay = pygame.Surface(
                (WIDTH, HEIGHT),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 160)
            )

            self.screen.blit(
                overlay,
                (0, 0)
            )

            game_over_text = self.large_font.render(
                "GAME OVER",
                True,
                FOOD_COLOR
            )

            score_text = self.score_font.render(
                f"Final Score: {self.stats.score}",
                True,
                TEXT_COLOR
            )

            restart_text = self.small_font.render(
                "Press R to play again",
                True,
                SECONDARY_TEXT
            )

            self.screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(WIDTH // 2, HEIGHT // 2 - 60)
                )
            )

            self.screen.blit(
                score_text,
                score_text.get_rect(
                    center=(WIDTH // 2, HEIGHT // 2)
                )
            )

            self.screen.blit(
                restart_text,
                restart_text.get_rect(
                    center=(WIDTH // 2, HEIGHT // 2 + 45)
                )
            )

    # --------------------------------------------------------
    # DRAW EVERYTHING
    # --------------------------------------------------------

    def draw(self):

        self.screen.fill(BACKGROUND)

        self.draw_grid()

        self.draw_food()

        self.draw_snake()

        self.draw_ui()

        self.draw_overlay()

        pygame.display.flip()

    # --------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------

    def run(self):

        while self.running:

            delta_time = self.clock.tick(FPS)

            self.handle_events()

            self.update(delta_time)

            self.draw()

        pygame.quit()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    game = SnakeGame()

    game.run()
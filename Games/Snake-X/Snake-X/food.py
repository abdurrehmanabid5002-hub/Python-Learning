"""Food generation."""
import random
from settings import GRID_WIDTH, GRID_HEIGHT

class Food:
    def __init__(self,occupied=None):
        self.position=None; self.spawn(occupied or set())
    def spawn(self,occupied):
        free=[(x,y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if (x,y) not in occupied]
        self.position=random.choice(free) if free else None
    def respawn(self,snake): self.spawn(snake.occupied)

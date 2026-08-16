"""Game controller, rendering, scoring and persistence."""
from dataclasses import dataclass
import pygame
from food import Food
from snake import Snake
from settings import *

@dataclass
class GameStats:
    score:int=0
    high_score:int=0
    level:int=1

class SnakeGame:
    def __init__(self):
        pygame.init(); pygame.display.set_caption(WINDOW_TITLE)
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT)); self.clock=pygame.time.Clock()
        self.title_font=pygame.font.SysFont('arial',34,bold=True)
        self.score_font=pygame.font.SysFont('arial',24,bold=True)
        self.small_font=pygame.font.SysFont('arial',18); self.large_font=pygame.font.SysFont('arial',52,bold=True)
        self.snake=Snake(); self.food=Food(self.snake.occupied)
        self.stats=GameStats(high_score=self.load_high_score())
        self.running=True; self.paused=False; self.game_over=False; self.speed=START_SPEED; self.move_timer=0.0
    def load_high_score(self):
        try: return max(0,int(HIGH_SCORE_FILE.read_text(encoding='utf-8').strip()))
        except (OSError,ValueError): return 0
    def save_high_score(self):
        try:
            DATA_DIR.mkdir(parents=True,exist_ok=True); HIGH_SCORE_FILE.write_text(f'{self.stats.high_score}\n',encoding='utf-8')
        except OSError: pass
    def restart(self):
        self.snake.reset(); self.food.respawn(self.snake); self.stats.score=0; self.stats.level=1; self.speed=START_SPEED
        self.paused=False; self.game_over=False; self.move_timer=0.0
    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT: self.running=False
            elif event.type==pygame.KEYDOWN:
                if event.key in (pygame.K_UP,pygame.K_w): self.snake.change_direction(UP)
                elif event.key in (pygame.K_DOWN,pygame.K_s): self.snake.change_direction(DOWN)
                elif event.key in (pygame.K_LEFT,pygame.K_a): self.snake.change_direction(LEFT)
                elif event.key in (pygame.K_RIGHT,pygame.K_d): self.snake.change_direction(RIGHT)
                elif event.key==pygame.K_SPACE and not self.game_over: self.paused=not self.paused
                elif event.key==pygame.K_r: self.restart()
                elif event.key==pygame.K_ESCAPE: self.running=False
    def update(self,dt):
        if self.paused or self.game_over: return
        self.move_timer += dt; interval=1000/self.speed
        if self.move_timer<interval: return
        self.move_timer-=interval; self.snake.move()
        if self.snake.hits_wall() or self.snake.hits_self(): self.end_game(); return
        if self.snake.head==self.food.position:
            self.snake.grow(); self.stats.score+=10; self.stats.high_score=max(self.stats.high_score,self.stats.score)
            self.food.respawn(self.snake); self.update_level()
    def update_level(self):
        self.stats.level=self.stats.score//50+1
        self.speed=min(START_SPEED+(self.stats.level-1)*1.5,MAX_SPEED)
    def end_game(self): self.game_over=True; self.stats.high_score=max(self.stats.high_score,self.stats.score); self.save_high_score()
    def draw_grid(self):
        for x in range(0,WIDTH,CELL_SIZE): pygame.draw.line(self.screen,GRID_COLOR,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,CELL_SIZE): pygame.draw.line(self.screen,GRID_COLOR,(0,y),(WIDTH,y))
    def draw_snake(self):
        for i,(x,y) in enumerate(self.snake.body):
            r=pygame.Rect(x*CELL_SIZE+2,y*CELL_SIZE+2,CELL_SIZE-4,CELL_SIZE-4)
            pygame.draw.rect(self.screen,SNAKE_HEAD if i==0 else SNAKE_BODY,r,border_radius=7)
            if i==0: self.draw_eyes(r)
    def draw_eyes(self,r):
        if self.snake.direction==RIGHT: eyes=[(r.right-8,r.top+6),(r.right-8,r.bottom-6)]
        elif self.snake.direction==LEFT: eyes=[(r.left+8,r.top+6),(r.left+8,r.bottom-6)]
        elif self.snake.direction==UP: eyes=[(r.left+6,r.top+8),(r.right-6,r.top+8)]
        else: eyes=[(r.left+6,r.bottom-8),(r.right-6,r.bottom-8)]
        for e in eyes: pygame.draw.circle(self.screen,BACKGROUND,e,4)
    def draw_food(self):
        if self.food.position is None: return
        x,y=self.food.position; c=(x*CELL_SIZE+CELL_SIZE//2,y*CELL_SIZE+CELL_SIZE//2)
        pygame.draw.circle(self.screen,FOOD_COLOR,c,CELL_SIZE//2-4); pygame.draw.circle(self.screen,FOOD_HIGHLIGHT,(c[0]-4,c[1]-4),3)
    def draw_ui(self):
        items=[('SNAKE X',20,12,self.title_font), (f'Score: {self.stats.score}',220,18,self.score_font),(f'Best: {self.stats.high_score}',390,18,self.score_font),(f'Level: {self.stats.level}',560,18,self.score_font)]
        for text,x,y,font in items: self.screen.blit(font.render(text,True,TEXT_COLOR),(x,y))
        self.screen.blit(self.small_font.render('WASD / Arrows  •  SPACE: Pause  •  R: Restart  •  ESC: Quit',True,SECONDARY_TEXT),(20,HEIGHT-30))
    def draw_overlay(self):
        if not(self.paused or self.game_over): return
        overlay=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA); overlay.fill((0,0,0,155)); self.screen.blit(overlay,(0,0))
        heading=self.large_font.render('PAUSED' if self.paused else 'GAME OVER',True,PAUSE_COLOR if self.paused else FOOD_COLOR)
        message=self.small_font.render('Press SPACE to continue' if self.paused else f'Final Score: {self.stats.score}   •   Press R to restart',True,TEXT_COLOR)
        self.screen.blit(heading,heading.get_rect(center=(WIDTH//2,HEIGHT//2-35))); self.screen.blit(message,message.get_rect(center=(WIDTH//2,HEIGHT//2+30)))
    def draw(self):
        self.screen.fill(BACKGROUND); self.draw_grid(); self.draw_food(); self.draw_snake(); self.draw_ui(); self.draw_overlay(); pygame.display.flip()
    def run(self):
        while self.running:
            dt=self.clock.tick(FPS); self.handle_events(); self.update(dt); self.draw()
        self.save_high_score(); pygame.quit()

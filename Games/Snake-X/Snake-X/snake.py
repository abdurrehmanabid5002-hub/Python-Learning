"""Snake data structure and movement logic."""
from collections import deque
from settings import *

class Snake:
    """Uses deque for O(1) head/tail updates and set for O(1) average membership."""
    def __init__(self): self.reset()
    def reset(self):
        cx,cy=GRID_WIDTH//2,GRID_HEIGHT//2
        self.body=deque([(cx,cy),(cx-1,cy),(cx-2,cy)])
        self.occupied=set(self.body)
        self.direction=self.next_direction=RIGHT
        self.growing=False
    @property
    def head(self): return self.body[0]
    @property
    def length(self): return len(self.body)
    def change_direction(self,new_direction):
        if new_direction in OPPOSITE_DIRECTION and new_direction != OPPOSITE_DIRECTION[self.direction]:
            self.next_direction=new_direction
    def move(self):
        self.direction=self.next_direction
        x,y=self.head; dx,dy=self.direction
        new_head=(x+dx,y+dy)
        self.body.appendleft(new_head); self.occupied.add(new_head)
        if not self.growing:
            self.occupied.remove(self.body.pop())
        self.growing=False
    def grow(self): self.growing=True
    def hits_wall(self):
        x,y=self.head
        return x<0 or x>=GRID_WIDTH or y<0 or y>=GRID_HEIGHT
    def hits_self(self):
        head=self.head; self.occupied.remove(head)
        hit=head in self.occupied; self.occupied.add(head)
        return hit

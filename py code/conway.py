# Code 1: Conway's Game of Life in 10 lines
import random
w,h=40,20
grid=[[random.choice([0,1])for _ in range(w)]for _ in range(h)]
for gen in range(100):
    print('\n'.join(''.join('#' if cell else ' ' for cell in row) for row in grid))
    new=[[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            n=sum(grid[(y+dy)%h][(x+dx)%w] for dy in (-1,0,1) for dx in (-1,0,1) if (dx,dy)!=(0,0))
            new[y][x]=1 if (grid[y][x] and n in (2,3)) or (not grid[y][x] and n==3) else 0
    grid=new
    input("Press Enter for next generation...")


# Code 2: ASCII Mandelbrot set renderer (12 lines)
w,h=80,40
for y in range(h):
    line=''
    for x in range(w):
        c=complex(-2+x*3/w, -1+y*2/h)
        z=0
        for i in range(50):
            z=z*z+c
            if abs(z)>2:
                break
        line+=' .,:;+=xX$#'[min(i//5,9)]
    print(line)
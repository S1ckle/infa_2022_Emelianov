
#ОТРАЖЕНИЕ

import pygame
import random
from pygame.draw import *
from random import randint
pygame.init()

popal=0
FPS = 60
screen = pygame.display.set_mode((900, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = 600
y = 200
dy = 10
dx = 10

def new_ball():
    '''
    создает движущийся шар, который отражается произвольно от стен
    '''
    global x, y, r
    global dx, dy
    if x < 50 or x > 850:
        dx*=-1
        x=x+dx
        dx += random.choice([-5, +5])
        dy += random.choice([-5, +5])
        if dx < -20:
            dx = -10
        if dx > 20:
            dx = 10
        if dy < -20:
            dy = -10
        if dy > 20:
            dy = 10
    if y < 50 or y > 850:
        dy*=-1
        y=y+dy
        dy += random.choice([-5, +5])
        dx += random.choice([-5, +5])
        if dx < -20:
            dx = -10
        if dx > 20:
            dx = 10
        if dy < -20:
            dy = -10
        if dy > 20:
            dy = 10
    x += dx
    y += dy
    if dx==0:
        dx=5
    if dy==0:
        dy=5
    r = 50
    circle(screen, YELLOW, (x, y), r)

def click(event):
    print(event.pos)
    print(x, y, r)

def rasstoyanie(a, b, c):
    if ((event.pos[0] - a) ** 2 + (event.pos[1] - b) ** 2) <= c ** 2:
        op=True
    else:
        op=False
    return(op)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                finished = True
                print(popal, "СЧЕТ")
            elif event.button == 1:
                click(event)
                if rasstoyanie(x, y, r) == True:
                    print("ПОПАЛ")
                    popal=popal+1
                else:
                    print("НЕ ПОПАЛ")
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)



pygame.quit()
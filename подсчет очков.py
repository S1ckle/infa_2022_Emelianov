
#ПОДСЧЕТ ОЧКОВ

import pygame
from pygame.draw import *
from random import randint
pygame.init()

popal=0
shar=0
FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

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
                print(popal,":" ,shar, "СЧЕТ")
            elif event.button == 1:
                click(event)
                if rasstoyanie(x, y, r) == True:
                    print("ПОПАЛ")
                    popal=popal+1
                else:
                    print("НЕ ПОПАЛ")
    new_ball()
    shar=shar+1
    pygame.display.update()
    screen.fill(BLACK)



pygame.quit()
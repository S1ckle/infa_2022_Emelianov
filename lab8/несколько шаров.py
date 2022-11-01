
#НЕСКОЛЬКО ШАРОВ

import pygame
from pygame.draw import *
from random import randint
pygame.init()

popal=0
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
x=0
y=0
r=0
def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ball1():
    global x1, y1, r1
    x1 = randint(100,700)
    y1 = randint(100,500)
    r1 = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x1, y1), r1)

def new_ball2():
    global x2, y2, r2
    x2 = randint(100,700)
    y2 = randint(100,500)
    r2 = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x2, y2), r2)


def click(event):
    print(event.pos)
    print(x, y, r)

def click1(event):
    print(x1, y1, r1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

def rasstoyanie(a, b, c):
    if ((event.pos[0] - a) ** 2 + (event.pos[1] - b) ** 2) <= c ** 2:
        op=True
    else:
        op=False
    return(op)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                finished = True
                print(popal, "СЧЕТ")
            elif event.button == 1:
                click(event)
                click1(event)
                if rasstoyanie(x, y, r) == True:
                    print("ПОПАЛ")
                    popal=popal+1
                elif rasstoyanie(x1, y1, r1) == True:
                    print("ПОПАЛ")
                    popal=popal+1
                elif rasstoyanie(x2, y2, r2) == True:
                    print("ПОПАЛ")
                    popal=popal+1
                else:
                    print("НЕ ПОПАЛ")
    new_ball()
    new_ball1()
    new_ball2()
    pygame.display.update()
    screen.fill(BLACK)



pygame.quit()
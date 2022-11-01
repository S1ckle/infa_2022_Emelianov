import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill([255,120,10])

circle(screen, (255, 255, 0), (200, 175), 100)

line(screen, (0, 0, 0), (150, 250), (250, 250), 20)

circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (255, 0, 0), (250, 150), 20)

circle(screen, (0, 0, 0), (150, 150), 5)
circle(screen, (0, 0, 0), (250, 150), 5)

line(screen, (0, 0, 0), (120, 110), (170, 130), 10)
line(screen, (0, 0, 0), (230, 130), (280, 110), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

gray = [192, 192, 192]
screen.fill(gray)

def face ():
    circle(screen, (255, 255, 0), (200, 175), 100)
    circle(screen, (0, 0, 0), (200, 175), 100, 1)
face ()

def eye_left ():
    circle(screen, (255, 0, 0), (150, 150), 22)
    circle(screen, (0, 0, 0), (150, 150), 8)
    circle(screen, (0, 0, 0), (150, 150), 22,1)

eye_left ()

def eye_right ():
    circle(screen, (255, 0, 0), (250, 150), 17)
    circle(screen, (0, 0, 0), (250, 150), 8)
    circle(screen, (0, 0, 0), (250, 150), 17,1)
eye_right ()

def mouth ():
    rect(screen, (0, 0, 0), (160, 230, 80, 15), 10)
mouth ()


def brow_left ():
    line(screen, (0, 0, 0), (100, 100), (180, 135), 10)
brow_left ()

def brow_right ():
    line(screen, (0, 0, 0), (230, 135), (280, 110), 10)
brow_right ()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

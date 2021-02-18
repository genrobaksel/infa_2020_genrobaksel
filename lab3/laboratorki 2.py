import pygame
from pygame.draw import *
import sys

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

green = [0, 128, 0]
screen.fill(green)
BLACK = [0,0,0]
red = [255,0,0]

def sky ():
        rect (screen, (0,255,255), (0,0,800,300))

sky ()

def house_main ():
    rect(screen, (0, 0, 0), (130, 230, 200, 180), 5)
    rect(screen, (128, 128, 0), (130, 230, 200, 180))

house_main()

def house_window ():
    rect(screen, (210, 105, 30), (200, 290, 60, 60), 5)
    rect(screen, (0, 0, 250), (200, 290, 60, 60))
    
house_window()

def house_roof ():
    
    polygon(screen, red,[[130,230], [330,230], [230,130]])
    lines(screen, BLACK, True, [[130,230], [330,230], [230,130]], 4)
    
    
house_roof()

def sky (x,y,z):
        
        for i2 in range (4):
                circle(screen, (255, 255, 255), (600 +x +y , 135),30)
                circle(screen, (0, 0, 0), (600 +x +y , 135),30, 2)
                x = x+40
        for i3 in range (2):
                circle(screen, (255, 255, 255), (840 -x +y, 115),30)
                circle(screen, (0, 0, 0), (840 -x +y , 115),30, 2)
                x = x+40
               
                         
                
        
sky (0,0,2)

def tree_trunk ():
        line(screen,BLACK,[600,260],[600,400],20)

tree_trunk ()

def tree_leafs ():
        for i in range (1):
                circle(screen, (0, 100, 0), (600  , 225),30)
                circle(screen, (0, 0, 0), (600  , 225),30, 2)
                circle(screen, (0, 100, 0), (620  , 245),30)
                circle(screen, (0, 0, 0), (620  , 245),30, 2)
                circle(screen, (0, 100, 0), (580  , 245),30)
                circle(screen, (0, 0, 0), (580  , 245),30, 2)
                for i in range (20):
        

tree_leafs ()

def sun ():
        circle(screen, (255, 20, 147), (400  , 125),50)
        circle(screen, (0, 0, 0), (400  , 125),50, 2)
        
sun ()
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

#implementing dda using pygame
import pygame   
import sys
from pygame.locals import *
from dda import dda


pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('DDA Line Drawing Algorithm')


dda(0,0,500,500,window)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

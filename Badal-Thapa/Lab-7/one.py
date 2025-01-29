# learn to draw basic shapes using PyGame drawing functions.

import pygame

# initialize pygame
pygame.init()

# create window
width = 850
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Shapes")

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# main loop
running = True
while running:

    # event handliing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # filling screen with white color
    screen.fill((255, 255, 255))
    
    # draw different shapes
    # rectangle
    pygame.draw.rect(screen, RED, (50, 50, 100, 100))
    
    # circle
    pygame.draw.circle(screen, BLUE, (300, 100), 50)
    
    # line
    pygame.draw.line(screen, GREEN, (500, 50), (600, 150), 5)
    
    # polygon
    points = [(700, 50), (750, 100), (700, 150), (650, 100)]
    pygame.draw.polygon(screen, BLACK, points)
    
    # update dispplay
    pygame.display.flip()

pygame.quit()
# pygame window & understand the basic program structure.

import pygame

# initialize pygame
pygame.init()

# create window
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyGame Window")

# main loop
running = True
while running:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # filling screen with color
    screen.fill((135, 206, 235))

    # update display
    pygame.display.flip()

# quit pygameame
pygame.quit()
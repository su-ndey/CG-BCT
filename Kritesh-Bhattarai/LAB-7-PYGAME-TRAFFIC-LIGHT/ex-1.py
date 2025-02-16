import pygame
pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((0, 255, 245))

pygame.display.flip()

pygame.quit()

# Exercise 1: Creating a Basic Window
import pygame

# Initialize Pygame
pygame.init()

# Create window
width = 900
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame in Window")
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with  color
    screen.fill((0,255, 255))
    
    # Update display
    pygame.display.flip()
pygame.quit()






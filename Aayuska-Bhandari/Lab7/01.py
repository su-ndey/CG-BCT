
# Exercise 1: Basic Pygame Window
import pygame

# Initialize Pygame
pygame.init()

# Create window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Window")

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Fill screen with white color
    screen.fill((255, 255, 255))
   
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

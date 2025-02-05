# Exercise 1: Basic Pygame Window
# Objective: Create your first Pygame window and understand the basic program structure.

# Exercise 1: Creating a Basic Window
import pygame

# Initialize Pygame
pygame.init()

# Create window
width = 400
height = 400
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
    screen.fill((45 , 90 , 135))
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

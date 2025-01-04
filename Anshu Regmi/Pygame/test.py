import pygame

# Initialize Pygame
pygame.init()

# Create a screen of size 800x600
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Test Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detect window close event
            running = False

    # Fill the screen with a color (white)
    screen.fill((255, 255, 255))
    pygame.display.update()  # Refresh the screen

pygame.quit()

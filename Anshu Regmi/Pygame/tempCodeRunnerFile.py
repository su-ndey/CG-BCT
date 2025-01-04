import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(r'C:\Users\HP\Desktop\Pygame\ufo.jpg')
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load(r'C:\Users\HP\Desktop\Pygame\space-invaders.png')
playerX=370
playerY=480

def player():
    screen.blit(playerImg,(playerX,playerY))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional, e.g., black background)
    
    player()
    # Update the display
    pygame.display.update()  # This ensures the screen updates properly

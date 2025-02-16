import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((100, 100, 100))
    
    # Draw different shapes
    # Rectangle
    pygame.draw.rect(screen, [50,50,50], (0,0,200,400))
    pygame.draw.rect(screen, [0,0,0], (20,20,150,350))
    # Circle
    pygame.draw.circle(screen, [64,0,0], (95, 90), 50)
    pygame.draw.circle(screen, [64,64,0], (95, 200), 50)
    pygame.draw.circle(screen, GREEN, (95, 310), 50)
    

    
    pygame.display.flip()

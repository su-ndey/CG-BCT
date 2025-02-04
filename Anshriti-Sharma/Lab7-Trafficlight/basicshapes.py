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
    
    screen.fill((255, 255, 255))
    
    # Rectangle
    pygame.draw.rect(screen, RED, (50, 50, 100, 100))
    
    # Circle
    pygame.draw.circle(screen, BLUE, (300, 100), 50)
    
    # Line
    pygame.draw.line(screen, GREEN, (500, 50), (600, 150), 5)
    
    # Polygon
    points = [(700, 50), (750, 100), (700, 150), (650, 100)]
    pygame.draw.polygon(screen, BLACK, points)
    
    pygame.display.flip()


pygame.quit()

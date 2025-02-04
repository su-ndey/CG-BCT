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
    
 
    
    # Circle
    pygame.draw.circle(screen, BLUE, (300, 100), 50)
    pygame.draw.circle(screen, GREEN, (100, 100), 50)
    pygame.draw.circle(screen, RED, (200, 100), 50)
    pygame.draw.polygon(screen, (128, 0, 128), [(100, 100), (150, 50), (200, 100)], 0) 

    
    
   
    
   
    
    pygame.display.flip()


pygame.quit()

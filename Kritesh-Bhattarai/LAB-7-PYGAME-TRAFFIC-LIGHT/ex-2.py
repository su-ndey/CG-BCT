import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Drawing Shapes")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((255, 255, 255))

# Draw a rectangle
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))

    # Draw a circle
pygame.draw.circle(screen, (0, 255, 0), (400, 400), 100)

    # Draw a line
pygame.draw.line(screen, (0, 0, 255), (500, 500), (700, 700), 5)

    # Draw a polygon
pygame.draw.polygon(screen, (255, 255, 0), [(100, 500), (200, 600), (200, 700), (100, 700)])

pygame.display.flip()

pygame.quit()
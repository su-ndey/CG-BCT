import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Traffic Light")
GREY = (30, 30, 30)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY, (250, 50, 300, 700))
    pygame.draw.rect(screen, BLACK, (300, 100, 200, 600))

    current_time = pygame.time.get_ticks()
    if current_time % 3000 < 1000:
        pygame.draw.circle(screen, RED, (400, 200), 80)
    elif current_time % 3000 < 2000:
        pygame.draw.circle(screen, YELLOW, (400, 400), 80)
    else:
        pygame.draw.circle(screen, GREEN, (400, 600), 80)

    pygame.display.update()

pygame.quit()
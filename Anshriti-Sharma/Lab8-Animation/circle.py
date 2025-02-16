import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Shapes")
clock = pygame.time.Clock()

x = 400
y = 300
speed = 5
radius = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    # Move left, but don't go past the left boundary
    if keys[pygame.K_LEFT]:
        if x - radius > 0:
            x -= speed
    
    # Move right, but don't go past the right boundary
    if keys[pygame.K_RIGHT]:
        if x + radius < 800:
            x += speed
    
    # Move up, but don't go past the top boundary
    if keys[pygame.K_UP]:
        if y - radius > 0:
            y -= speed
    
    # Move down, but don't go past the bottom boundary
    if keys[pygame.K_DOWN]:
        if y + radius < 600:
            y += speed
    
    screen.fill((0, 0, 0))
    
    pygame.draw.circle(screen, (200, 162, 200), (int(x), int(y)), radius)
    
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()

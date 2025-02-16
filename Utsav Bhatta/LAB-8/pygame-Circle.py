import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Shapes")
clock = pygame.time.Clock()

# Object properties
x = 400
y = 300
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    screen.fill((255, 255, 255))
    
    # Draw moving circle
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 30)
    
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()

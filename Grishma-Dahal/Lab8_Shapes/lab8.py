import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Shapes with Boundaries")
clock = pygame.time.Clock()

# Object properties0
x = 400
y = 300
radius = 30  # Circle radius
speed = 5

# Screen boundaries
screen_width, screen_height = 800, 600

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius > 0:  # Left boundary
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius < screen_width:  # Right boundary
        x += speed
    if keys[pygame.K_UP] and y - radius > 0:  # Top boundary
        y -= speed
    if keys[pygame.K_DOWN] and y + radius < screen_height:  # Bottom boundary
        y += speed

    screen.fill((255, 255, 255))
    
    # Draw moving circle
    pygame.draw.circle(screen, (0, 153, 153), (int(x), int(y)), radius)
    
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
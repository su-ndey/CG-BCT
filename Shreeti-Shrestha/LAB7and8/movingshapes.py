import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Shapes with Boundaries")
clock = pygame.time.Clock()


x = 400
y = 300
radius = 30  
speed = 5


screen_width, screen_height = 800, 600

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius > 0:  
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius < screen_width: 
        x += speed
    if keys[pygame.K_UP] and y - radius > 0: 
        y -= speed
    if keys[pygame.K_DOWN] and y + radius < screen_height:  
        y += speed

    screen.fill((255, 255, 255))
    

    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), radius)
    
    pygame.display.flip()
    clock.tick(60)  
pygame.quit()


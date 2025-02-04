# understand basic animation by moving shapes across the screen

import pygame

# initialize pygame
pygame.init()

# create window
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Shapes")
clock = pygame.time.Clock()

# object properties
x = 400
y = 300
speed = 5
radius = 30  # radius of the circle

# main loop
running = True
while running:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # boundary checks to ensure the circle stays within the window
    if x - radius < 0:
        x = radius
    if x + radius > width:
        x = width - radius
    if y - radius < 0:
        y = radius
    if y + radius > height:
        y = height - radius
    
    # filling screen with white color
    screen.fill((255, 255, 255))
    
    # draw moving circle
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    
    # update display
    pygame.display.flip()

    clock.tick(60)  # Limit to 60 FPS

pygame.quit()

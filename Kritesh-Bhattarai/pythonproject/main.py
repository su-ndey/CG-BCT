import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
dt=0
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width()//2, screen.get_height()//2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, ("white"), player_pos, 100)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300*dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300*dt
    if keys[pygame.K_UP]:
        player_pos.y -= 300*dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300*dt
    pygame.display.update()
    dt = clock.tick(60)/1000
    print(dt)

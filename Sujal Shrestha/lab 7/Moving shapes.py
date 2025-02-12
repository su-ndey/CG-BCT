import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Moving Shapes")
clock = pg.time.Clock()

x = 400
y = 300
speed = 5
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= speed
    if keys[pg.K_RIGHT]:
        x += speed
    if keys[pg.K_UP]:
        y -= speed
    if keys[pg.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))
    pg.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 30)
    pg.display.flip()

    clock.tick(60)

pg.quit()

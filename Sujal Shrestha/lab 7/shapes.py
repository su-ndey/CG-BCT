import pygame as pg
pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Drawing Shapes")

BLACK = (0,0,0)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255,255,255))
    pg.draw.rect(screen,RED,(50,50,100,100))
    pg.draw.circle(screen,BLUE,(300,100),50)
    pg.draw.line(screen,GREEN,(500,50),(600,150),5)
    points= [(700,50),(750,100),(700,150),(650,100)]
    pg.draw.polygon(screen,BLACK,points)
    pg.display.flip()
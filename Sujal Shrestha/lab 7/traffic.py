import pygame as pg
pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Traffic Lights")
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(100,100,100)
running= True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:    
           running = False

    screen.fill((0,0,0))
    pg.draw.rect(screen,WHITE,(250,200,100,200))
    pg.draw.circle(screen,RED,(300,230),30)
    pg.draw.circle(screen,YELLOW,(300,300),30)
    pg.draw.circle(screen,GREEN,(300,370),30)

    pg.display.flip()

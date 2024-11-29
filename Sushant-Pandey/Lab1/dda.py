import pygame

def dda(x1,y1,x2,y2,window):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        pygame.draw.circle(window, (255,255,255), (round(x), round(y)), 1)        
        x += xinc
        y += yinc
        pygame.display.update()
    pygame.display.update()
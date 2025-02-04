import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Light")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DIM_RED = (128, 0, 0)
GREEN = (0, 255, 0)
DIM_GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DIM_YELLOW = (128, 128, 0)
ORANGE = (255,140,0)
beige = (245,245,220)
DIM_ORANGE = (204,102,0)

font = pygame.font.Font(None, 40)


red_circle = {"pos": (375, 150), "radius": 60, "color": RED, "dim_color": DIM_RED}
orange_circle = {"pos": (375, 300), "radius": 60, "color": ORANGE, "dim_color": DIM_ORANGE}
green_circle = {"pos": (375, 450), "radius": 60, "color": GREEN, "dim_color": DIM_GREEN}

lights = [red_circle, orange_circle, green_circle]  
messages = ["Stop", "Ready", "Go"]
current_light_index = 0
last_switch_time = pygame.time.get_ticks()
switch_interval = 2000 

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    current_time = pygame.time.get_ticks()
    if current_time - last_switch_time >= switch_interval:
        current_light_index = (current_light_index + 1) % len(lights)
        last_switch_time = current_time


    active_circle = lights[current_light_index]
    message = messages[current_light_index]


    screen.fill(beige)
    pygame.draw.rect(screen, beige, (240, 40, 270,520))
    pygame.draw.rect(screen, BLACK, (250, 50, 250, 500))

    for circle in lights:
        pygame.draw.circle(screen,
                           circle["color"] if circle == active_circle else circle["dim_color"],
                           circle["pos"], circle["radius"])

 
    if message:
        text = font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(75, 30))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()


# create Traffic Light System Using PyGame

import pygame

# initialize PyGame
pygame.init()

# create window
width = 800
height = 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Light")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DIM_RED = (128, 0, 0)
GREEN = (0, 255, 0)
DIM_GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DIM_YELLOW = (128, 128, 0)
GRAY = (128, 128, 128)

# Set font for text
font = pygame.font.Font(None, 40)

# Define circles for traffic lights with positions, radii, and colors
red_circle = {"pos": (375, 150), "radius": 60, "color": RED, "dim_color": DIM_RED}
yellow_circle = {"pos": (375, 300), "radius": 60, "color": YELLOW, "dim_color": DIM_YELLOW}
green_circle = {"pos": (375, 450), "radius": 60, "color": GREEN, "dim_color": DIM_GREEN}

# List of light circles and corresponding messages
lights = [red_circle, yellow_circle, green_circle]  
messages = ["Stop", "Ready", "Go"]

# Initialize the current light index and timing
current_light_index = 0
last_switch_time = pygame.time.get_ticks()
switch_interval = 2000  # Switch lights every 2000 ms (2 seconds)

# Main loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if it's time to switch the light
    current_time = pygame.time.get_ticks()
    if current_time - last_switch_time >= switch_interval:
        current_light_index = (current_light_index + 1) % len(lights)
        last_switch_time = current_time

    # Get the active circle and message for the current light
    active_circle = lights[current_light_index]
    message = messages[current_light_index]

    # Fill the background screen with a color
    screen.fill((211, 211, 211))

    # Draw the traffic light box
    pygame.draw.rect(screen, GRAY, (240, 40, 270, 520))
    pygame.draw.rect(screen, BLACK, (250, 50, 250, 500))

    # Draw the circles for the lights, highlighting the active light
    for circle in lights:
        pygame.draw.circle(screen, circle["color"] if circle == active_circle else circle["dim_color"], circle["pos"], circle["radius"])

    # Render and display the message
    if message:
        text = font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(75, 30))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit PyGame
pygame.quit()

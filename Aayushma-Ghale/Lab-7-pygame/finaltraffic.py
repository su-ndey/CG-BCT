import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Light Simulation")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Dimmed colors
DIMMED_RED = (128, 0, 0)
DIMMED_YELLOW = (128, 128, 0)
DIMMED_GREEN = (0, 128, 0)

# Fonts
font = pygame.font.SysFont(None, 48)  

# Variables for the traffic light state and timing
current_light = "red"
light_duration = {
    "red": 5000,    # 5 seconds
    "yellow": 2000, # 2 seconds
    "green": 5000   # 5 seconds
}
last_switch_time = pygame.time.get_ticks()

# Main loop
running = True
while running:
    screen.fill(BLACK)
    current_time = pygame.time.get_ticks()

    # Checking for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing traffic light box
    pygame.draw.rect(screen, GRAY, (290, 90, 220, 420))
    pygame.draw.rect(screen, BLACK, (300, 100, 200, 400))

    # Changing the light based on time
    elapsed_time = current_time - last_switch_time
    if elapsed_time > light_duration[current_light]:
        if current_light == "red":
            current_light = "yellow"
        elif current_light == "green":
            current_light = "red"
        elif current_light == "yellow":
            current_light = "green"
        last_switch_time = current_time

    # Calculating Remaining Time
    remaining_time = max(0, (light_duration[current_light] - elapsed_time) // 1000)

    # Determining the Next Light
    if current_light == "red":
        next_light = "STOP"
    elif current_light == "yellow":
        next_light = "WAIT"
    elif current_light == "green":
        next_light = "GO"

    # Drawing the lights with dimmed colors
    red_color = RED if current_light == "red" else DIMMED_RED
    yellow_color = YELLOW if current_light == "yellow" else DIMMED_YELLOW
    green_color = GREEN if current_light == "green" else DIMMED_GREEN

    pygame.draw.circle(screen, red_color, (400, 180), 50)
    pygame.draw.circle(screen, yellow_color, (400, 300), 50)
    pygame.draw.circle(screen, green_color, (400, 420), 50)

    # Rendering and display the remaining time
    timer_text = font.render(f"Time: {remaining_time}s", True, WHITE)
    screen.blit(timer_text, (320, 500))

    # Rendering and display the next light text
    next_light_text = font.render(f"{next_light}", True, WHITE)
    screen.blit(next_light_text, (320, 550))  # Position below the timer

    # Updating the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

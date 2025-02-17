import pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Light Simulation")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DIM_RED = (128, 0, 0)
GREEN = (0, 255, 0)
DIM_GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DIM_YELLOW = (128, 128, 0)
MAROON = (153, 0, 0)
GRAY = (128, 135, 130)

# Font for displaying the message
font = pygame.font.Font(None, 50)

# Circle definitions
red_circle = {"pos": (415, 175), "radius": 50, "color": RED, "dim_color": DIM_RED, "message": "Stop"}
yellow_circle = {"pos": (415, 300), "radius": 50, "color": YELLOW, "dim_color": DIM_YELLOW, "message": "Ready"}
green_circle = {"pos": (415, 425), "radius": 50, "color": GREEN, "dim_color": DIM_GREEN, "message": "Go"}

# Traffic light sequence
circles = [red_circle, yellow_circle, green_circle]
current_index = 0  # Start with red
timer_interval = 2000  # 2000 milliseconds (2 seconds) for each state
last_time = pygame.time.get_ticks()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check the timer
    current_time = pygame.time.get_ticks()
    if current_time - last_time > timer_interval:
        current_index = (current_index + 1) % len(circles)  # Move to the next state
        last_time = current_time

    active_circle = circles[current_index]
    message = active_circle["message"]

    # Fill the screen with background color
    screen.fill((194, 234, 233))
    
    # Draw the rectangle
    pygame.draw.rect(screen, GRAY, (280, 70, 270, 470))
    pygame.draw.rect(screen, BLACK, (290, 80, 250, 450))
    
    # Draw the circles
    pygame.draw.circle(screen, 
                       green_circle["color"] if active_circle == green_circle else green_circle["dim_color"], 
                       green_circle["pos"], green_circle["radius"])
    pygame.draw.circle(screen, 
                       yellow_circle["color"] if active_circle == yellow_circle else yellow_circle["dim_color"], 
                       yellow_circle["pos"], yellow_circle["radius"])
    pygame.draw.circle(screen, 
                       red_circle["color"] if active_circle == red_circle else red_circle["dim_color"], 
                       red_circle["pos"], red_circle["radius"])
    
    # Display the message
    if message:
        text = font.render(message, True, MAROON)
        text_rect = text.get_rect(center=(100, 60))
        screen.blit(text, text_rect)
    
    # Update the display
    pygame.display.flip()

pygame.quit()

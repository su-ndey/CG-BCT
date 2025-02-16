import pygame
import time

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Traffic Light System")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up traffic light positions
light_radius = 50
light_x = 200
light_y = 150
spacing = 100

# Set up font for text
font = pygame.font.SysFont('Arial', 36)

# Create clock object for controlling frame rate
clock = pygame.time.Clock()

# Define a function to draw the traffic light and message
def draw_traffic_light(color, message):
    # Fill background with white
    screen.fill(WHITE)

    # Draw traffic light container (rectangle)
    pygame.draw.rect(screen, BLACK, (light_x - 75, light_y - 75, 150, 350))

    # Draw red light
    pygame.draw.circle(screen, RED if color == "red" else (100, 0, 0), (light_x, light_y), light_radius)
    # Draw yellow light
    pygame.draw.circle(screen, YELLOW if color == "yellow" else (100, 100, 0), (light_x, light_y + spacing), light_radius)
    # Draw green light
    pygame.draw.circle(screen, GREEN if color == "green" else (0, 100, 0), (light_x, light_y + 2 * spacing), light_radius)

    # Render message
    text_surface = font.render(message, True, BLACK)
    screen.blit(text_surface, (light_x - text_surface.get_width() // 2, light_y + 3 * spacing))

    # Update display
    pygame.display.flip()

# Main loop
running = True
light_cycle = ["red", "green", "yellow"]
messages = ["STOP!!", "GO!!", "WAIT!!"]
current_light = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the traffic light with the current light and message
    draw_traffic_light(light_cycle[current_light], messages[current_light])
    
    # Switch to the next light in the cycle
    current_light = (current_light + 1) % 3  # Cycle through 0, 1, 2
    
    # Wait for 2 seconds before changing the light (adjust timing as needed)
    time.sleep(15)
# Quit Pygame
pygame.quit()
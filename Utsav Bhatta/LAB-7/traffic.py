import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Light")

# Colors
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARK_RED = (139, 0, 0)
DARK_YELLOW = (139, 139, 0)
DARK_GREEN = (0, 100, 0)
WHITE = (255, 255, 255)

# Font
small_font = pygame.font.Font(None, 36)

# Draw the traffic light
def draw_traffic_light(active_light):
    # Background
    screen.fill(GRAY)
    
    # Traffic light frame
    pygame.draw.rect(screen, BLACK, (125, 100, 150, 400))
    
    # Lights
    pygame.draw.circle(screen, RED if active_light == "red" else DARK_RED, (200, 180), 40)
    pygame.draw.circle(screen, YELLOW if active_light == "yellow" else DARK_YELLOW, (200, 300), 40)
    pygame.draw.circle(screen, GREEN if active_light == "green" else DARK_GREEN, (200, 420), 40)
    
    # Display "Go" when green
    if active_light == "green":
        go_text = small_font.render("Go", True, WHITE)
        screen.blit(go_text, (150, 470))

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    light_sequence = ["red", "yellow", "green"]  # Light order
    current_light_index = 0
    start_time = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check if 5 seconds have passed
        if time.time() - start_time >= 5:
            current_light_index = (current_light_index + 1) % len(light_sequence)
            start_time = time.time()

        # Get the current light
        active_light = light_sequence[current_light_index]

        # Draw the traffic light
        draw_traffic_light(active_light)

        # Update the display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

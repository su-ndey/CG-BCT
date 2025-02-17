import pygame
import time

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Light with Counter and Realistic Effects")

# Colors
RED, YELLOW, GREEN, GRAY, WHITE, BLACK, SHADOW = (
    (255, 0, 0), 
    (255, 255, 0), 
    (0, 255, 0), 
    (169, 169, 169), 
    (255, 255, 255), 
    (0, 0, 0), 
    (50, 50, 50)
)

# Circle positions and states
circle_x, circle_y, radius, spacing = 400, 150, 50, 120
state_colors, current_state = [RED, YELLOW, GREEN], 0

# Font setup
font = pygame.font.SysFont("BCD", 50)  # BCD-style font
counter_rect = pygame.Rect(510, 100, 60, 60)  # Positioned to the side of the traffic light
counter = 10

running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Timer logic
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:  # Update every second
        counter -= 1
        start_time = time.time()
    if counter == 0:
        current_state = (current_state + 1) % 3
        counter = 10 if current_state != 1 else 4  # Yellow stays for 4 seconds

    # Drawing logic
    screen.fill(WHITE)

    # Draw traffic light frame
    pygame.draw.rect(screen, GRAY, (290, 70, 220, 420), border_radius=20)
    pygame.draw.rect(screen, BLACK, (300, 80, 200, 400), border_radius=10)

    # Add partitions with shading
    for i in range(1, 3):
        partition_y = circle_y + (i * spacing) - (spacing // 2)

    # Draw circles
    for i, color in enumerate(state_colors):
        pygame.draw.circle(screen, color if i == current_state else GRAY, (circle_x, circle_y + i * spacing), radius)
        pygame.draw.circle(screen, SHADOW, (circle_x, circle_y + i * spacing), radius + 3, width=3)  # Add shadows

    # Counter display attached to the light block
    pygame.draw.rect(screen, BLACK, counter_rect, border_radius=10)
    counter_color = RED if current_state == 0 else GREEN if current_state == 2 else YELLOW
    counter_text = font.render(str(counter), True, counter_color)
    screen.blit(counter_text, (counter_rect.x + 10, counter_rect.y + 5))

    pygame.display.flip()

pygame.quit()
import pygame
import time

# Initialize Pygame
pygame.init()

# Create window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Light")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Define the positions and sizes for the traffic light
light_radius = 40
light_x = 400
light_y_start = 150

# Define font for displaying text
font = pygame.font.SysFont(None, 48)

# Function to draw the traffic light
def draw_traffic_light(state):
    screen.fill(WHITE)  # Set the background to white
    
    # Draw the black outline of the traffic light
    pygame.draw.rect(screen, BLACK, (light_x - 75, light_y_start - 50, 150, 300))
    
    # Draw the three circles (lights)
    pygame.draw.circle(screen, RED if state == 'red' else (100, 0, 0), (light_x, light_y_start), light_radius)  # Red light
    pygame.draw.circle(screen, YELLOW if state == 'yellow' else (200, 200, 0), (light_x, light_y_start + 100), light_radius)  # Yellow light
    pygame.draw.circle(screen, GREEN if state == 'green' else (0, 100, 0), (light_x, light_y_start + 200), light_radius)  # Green light

# Function to display the text (STOP, WAIT, GO) based on the current state
def display_message(state):
    if state == "red":
        message = "STOP"
    elif state == "yellow":
        message = "WAIT"
    else:  # green
        message = "GO"
    
    # Render the message text
    text = font.render(message, True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, height - 100))  # Display text near the bottom of the screen

# Function to display the countdown timer
def display_timer(remaining_time):
    # Render the remaining time as text
    timer_text = font.render(f"Time: {int(remaining_time)}s", True, BLACK)
    screen.blit(timer_text, (width // 2 - timer_text.get_width() // 2, height - 150))  # Display timer above the message

# Main game loop
running = True
current_state = 'red'  # Start with the red light
state_duration = {'red': 5, 'yellow': 2, 'green': 5}  # Duration for each light
last_switch_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Changing the light based on time
    elapsed_time = time.time() - last_switch_time  # Get the actual elapsed time
    if elapsed_time > state_duration[current_state]:
        # Switch to the next light
        if current_state == "red":
            current_state = "yellow"
        elif current_state == "yellow":
            current_state = "green"
        elif current_state == "green":
            current_state = "red"
        
        last_switch_time = time.time()  # Reset the time for the next light

    # Calculate remaining time for the current state
    remaining_time = max(0, state_duration[current_state] - elapsed_time)

    # Draw the traffic light with the current state
    draw_traffic_light(current_state)

    # Display the message ("STOP", "WAIT", or "GO") for the current light
    display_message(current_state)

    # Display the countdown timer
    display_timer(remaining_time)
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

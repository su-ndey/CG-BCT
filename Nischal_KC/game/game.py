import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Fruits - Avoid the Bombs")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load images
background = pygame.image.load("bacground.png")  # Replace with your background image path
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale to full screen
bomb_icon = pygame.image.load("bomb_icon.png")  # Replace with your bomb icon path
bomb_icon = pygame.transform.scale(bomb_icon, (32, 32))  # Resize the bomb icon
fruit_icon = pygame.image.load("healthy.png")  # Replace with your fruit icon path
fruit_icon = pygame.transform.scale(fruit_icon, (32, 32))  # Resize the fruit icon

# Fonts
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player properties (basket)
basket_size = 100
basket_pos = [WIDTH // 2 - basket_size // 2, HEIGHT - 50]
basket_speed = 10

# Fruit properties
fruit_size = 30
num_fruits = 5
fruits = [{"pos": [random.randint(0, WIDTH - fruit_size), 0], "speed": random.randint(3, 7)} for _ in range(num_fruits)]

# Bomb properties
bomb_size = 30
num_bombs = 3
bombs = [{"pos": [random.randint(0, WIDTH - bomb_size), 0], "speed": random.randint(3, 6)} for _ in range(num_bombs)]

# Flash effect parameters
flash = False
flash_timer = 0
FLASH_DURATION = 300  # Duration of flash in milliseconds

# Detect collision
def detect_collision(basket_pos, obj_pos, obj_size):
    bx, by = basket_pos
    ox, oy = obj_pos

    return (bx < ox < bx + basket_size or bx < ox + obj_size < bx + basket_size) and (
        by < oy < by + 30 or by < oy + obj_size < by + 30
    )

def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def draw_fruit(pos):
    screen.blit(fruit_icon, pos)  # Draw the fruit icon

def draw_bomb(pos):
    screen.blit(bomb_icon, pos)  # Draw the bomb icon

def starting_screen():
    screen.fill(WHITE)
    title = large_font.render("Catch the Fruits", True, GREEN)
    instruction = font.render("Press SPACE to Start", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def game_over_screen(final_score):
    screen.fill(WHITE)
    title = large_font.render("Game Over", True, RED)
    score_text = font.render(f"Your Score: {final_score}", True, BLACK)
    instruction = font.render("Press R to Restart or Q to Quit", True, BLACK)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    return True
                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    exit()

# Main Game Loop
while True:
    starting_screen()

    # Reset game variables
    basket_pos = [WIDTH // 2 - basket_size // 2, HEIGHT - 50]
    fruits = [{"pos": [random.randint(0, WIDTH - fruit_size), 0], "speed": random.randint(3, 7)} for _ in range(num_fruits)]
    bombs = [{"pos": [random.randint(0, WIDTH - bomb_size), 0], "speed": random.randint(3, 6)} for _ in range(num_bombs)]
    score = 0
    running = True

    while running:
        screen.blit(background, (0, 0))  # Draw the background image

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Basket movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_pos[0] > 0:
            basket_pos[0] -= basket_speed
        if keys[pygame.K_RIGHT] and basket_pos[0] < WIDTH - basket_size:
            basket_pos[0] += basket_speed

        # Fruit movement
        for fruit in fruits:
            fruit["pos"][1] += fruit["speed"]
            if fruit["pos"][1] > HEIGHT:
                fruit["pos"] = [random.randint(0, WIDTH - fruit_size), 0]

            if detect_collision(basket_pos, fruit["pos"], fruit_size):
                score += 1
                fruit["pos"] = [random.randint(0, WIDTH - fruit_size), 0]

        # Bomb movement
        for bomb in bombs:
            bomb["pos"][1] += bomb["speed"]
            if bomb["pos"][1] > HEIGHT:
                bomb["pos"] = [random.randint(0, WIDTH - bomb_size), 0]

            if detect_collision(basket_pos, bomb["pos"], bomb_size):
                running = False  # Game over

        # Draw basket, fruits, and bombs
        pygame.draw.rect(screen, GREEN, (*basket_pos, basket_size, 30))
        for fruit in fruits:
            draw_fruit(fruit["pos"])
        for bomb in bombs:
            draw_bomb(bomb["pos"])

        # Display score
        display_score(score)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)

    # Game over screen
    if not game_over_screen(score):
        break  # Quit if the player chooses not to restart

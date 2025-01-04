import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Racing Game")

# Load and resize images
car_img = pygame.image.load("car.png")  # Change to your car image
car_img = pygame.transform.scale(car_img, (50, 100))

obstacle_img = pygame.image.load("obstacle.png")  # Change to your obstacle image
obstacle_img = pygame.transform.scale(obstacle_img, (50, 50))

# Load sounds
engine_sound = pygame.mixer.Sound("car-engine.mp3")  # Engine sound
crash_sound = pygame.mixer.Sound("crash.mp3")    # Crash sound
pygame.mixer.music.load("car_racing_background.mp3")   # Background racing music

# Player settings
player_pos = [screen_width // 2 - 25, screen_height - 120]  # Initial car position
player_speed = 10

# Obstacle settings
obstacles = []
obstacle_speed = 5
obstacle_spawn_time = 1000  # milliseconds
last_obstacle_spawn = pygame.time.get_ticks()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

# Game states
PLAYING = 0
GAME_OVER = 1
WAITING_TO_START = 2
game_state = WAITING_TO_START

def reset_game():
    global player_pos, obstacles, last_obstacle_spawn, game_state, score
    player_pos = [screen_width // 2 - 25, screen_height - 120]
    obstacles = []
    last_obstacle_spawn = pygame.time.get_ticks()
    score = 0
    game_state = PLAYING

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Main game loop
running = True
pygame.mixer.music.play(-1)  # Play background music in a loop
while running:
    dt = clock.tick(60)  # Frame rate

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == WAITING_TO_START:
                reset_game()
                pygame.mixer.music.stop()  # Stop background music when game starts
            elif game_state == GAME_OVER and event.key == pygame.K_RETURN:
                game_state = WAITING_TO_START
                pygame.mixer.music.play(-1)  # Play background music again

    keys = pygame.key.get_pressed()
    if game_state == PLAYING:
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed

        # Ensure player car stays within screen boundaries
        if player_pos[0] < 0:
            player_pos[0] = 0
        if player_pos[0] > screen_width - car_img.get_width():
            player_pos[0] = screen_width - car_img.get_width()
        if player_pos[1] < 0:
            player_pos[1] = 0
        if player_pos[1] > screen_height - car_img.get_height():
            player_pos[1] = screen_height - car_img.get_height()

        # Obstacle spawning
        current_time = pygame.time.get_ticks()
        if current_time - last_obstacle_spawn > obstacle_spawn_time:
            obstacle_x = random.randint(0, screen_width - obstacle_img.get_width())
            obstacles.append([obstacle_x, 0])  # New obstacle at top
            last_obstacle_spawn = current_time

        # Obstacle movement
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > screen_height:
                obstacles.remove(obstacle)
                score += 1  # Increase score when obstacle goes off screen

        # Check for collision between player and obstacles
        for obstacle in obstacles:
            if player_pos[0] < obstacle[0] + obstacle_img.get_width() and player_pos[0] + car_img.get_width() > obstacle[0] and player_pos[1] < obstacle[1] + obstacle_img.get_height() and player_pos[1] + car_img.get_height() > obstacle[1]:
                game_state = GAME_OVER
                pygame.mixer.stop()  # Stop all sounds
                crash_sound.play()
                break

    # Drawing
    screen.fill((0, 251, 255,1))  # Background color (black)
    if game_state == PLAYING:
        screen.blit(car_img, player_pos)
        for obstacle in obstacles:
            screen.blit(obstacle_img, obstacle)
        draw_text(f"Score: {score}", font, (255, 255, 255), screen, 70, 20)
    elif game_state == GAME_OVER:
        draw_text("Game Over", pygame.font.Font(None, 74), (255, 0, 0), screen, screen_width // 2, screen_height // 2)
        draw_text(f"Final Score: {score}", pygame.font.Font(None, 36), (255, 255, 255), screen, screen_width // 2, screen_height // 2 + 50)
        draw_text("Press Enter to Restart", pygame.font.Font(None, 36), (255, 255, 255), screen, screen_width // 2, screen_height // 2 + 100)
    elif game_state == WAITING_TO_START:
        draw_text("Press Any Key to Start", pygame.font.Font(None, 36), (0, 0, 255,1), screen, screen_width // 2, screen_height // 2)

    pygame.display.flip()

pygame.quit()

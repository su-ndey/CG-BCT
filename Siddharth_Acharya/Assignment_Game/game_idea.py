import pygame
import random
import sys
import os

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
FONT = pygame.font.Font(None, 36)

# Game variables
player_speed = 10
bullet_speed = 10
enemy_speed = 2
asteroid_speed = 2
powerup_speed = 0.5
level = 1
score = 0
lives = 10  # Set the number of lives to 10
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 100
bullets = []
enemies = []
asteroids = []
powerups = []

# Load images
player_ship = pygame.image.load("fighter_plane.png")  # Load custom image for player
player_ship = pygame.transform.scale(player_ship, (50, 50))  # Scale it to the desired size

enemy_ship = pygame.image.load("enemy_plane.png")
enemy_ship = pygame.transform.scale(enemy_ship, (40, 40))

asteroid = pygame.image.load("asteroid.png")
asteroid = pygame.transform.scale(asteroid, (30, 30))

powerup_item = pygame.image.load("powerup.png")
powerup_item = pygame.transform.scale(powerup_item, (20, 20))

background = pygame.image.load("space.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock object
clock = pygame.time.Clock()

# Draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Draw player
def draw_player(x, y):
    screen.blit(player_ship, (x, y))

# Draw bullets
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

# Draw enemies
def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_ship, (enemy.x, enemy.y))

# Draw asteroids
def draw_asteroids():
    for asteroid_obj in asteroids:
        screen.blit(asteroid, (asteroid_obj.x, asteroid_obj.y))

# Draw powerups
def draw_powerups():
    for powerup_obj in powerups:
        screen.blit(powerup_item, (powerup_obj.x, powerup_obj.y))

# Bullet movement
def move_bullets():
    global score
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

        # Check collision with enemies
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                score += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

        # Check collision with asteroids
        for asteroid_obj in asteroids[:]:
            if bullet.colliderect(asteroid_obj):
                asteroids.remove(asteroid_obj)
                bullets.remove(bullet)
                break

# Enemy movement
def move_enemies():
    global lives
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)
            lives -= 1

# Asteroid movement
def move_asteroids():
    global lives
    for asteroid_obj in asteroids[:]:
        asteroid_obj.y += asteroid_speed
        if asteroid_obj.y > SCREEN_HEIGHT:
            asteroids.remove(asteroid_obj)
            lives -= 1

# Power-up movement
def move_powerups():
    for powerup_obj in powerups[:]:
        powerup_obj.y += powerup_speed
        if powerup_obj.y > SCREEN_HEIGHT:
            powerups.remove(powerup_obj)

# Generate random enemy
def generate_enemy():
    enemy = pygame.Rect(random.randint(50, SCREEN_WIDTH - 50), -40, 40, 40)
    enemies.append(enemy)

# Generate random asteroid
def generate_asteroid():
    asteroid_obj = pygame.Rect(random.randint(50, SCREEN_WIDTH - 50), -30, 30, 30)
    asteroids.append(asteroid_obj)

# Generate random power-up
def generate_powerup():
    powerup_obj = pygame.Rect(random.randint(50, SCREEN_WIDTH - 50), -20, 20, 20)
    powerups.append(powerup_obj)

# Restart the game by resetting the game variables
def restart_game():
    global score, lives, level, player_x, bullets, enemies, asteroids, powerups
    score = 0
    lives = 10
    level = 1
    player_x = SCREEN_WIDTH // 2
    bullets = []
    enemies = []
    asteroids = []
    powerups = []

# Main game loop
def main():
    global player_x, lives, level, score, bullets

    # Timer for generating new enemies and obstacles
    enemy_timer = 0
    asteroid_timer = 0
    powerup_timer = 0

    while True:
        screen.blit(background, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key press handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullet = pygame.Rect(player_x + 20, player_y, 10, 20)
            bullets.append(bullet)

        # Game mechanics
        move_bullets()
        move_enemies()
        move_asteroids()
        move_powerups()

        # Generate new enemies and obstacles
        enemy_timer += 1
        asteroid_timer += 1
        powerup_timer += 1

        if enemy_timer > 50:
            generate_enemy()
            enemy_timer = 0
        if asteroid_timer > 150:
            generate_asteroid()
            asteroid_timer = 0
        if powerup_timer > 300:
            generate_powerup()
            powerup_timer = 0

        # Draw everything
        draw_player(player_x, player_y)
        draw_bullets()
        draw_enemies()
        draw_asteroids()
        draw_powerups()

        # Display score and lives
        draw_text(f"Score: {score}", FONT, WHITE, screen, SCREEN_WIDTH // 2, 30)
        draw_text(f"Lives: {lives}", FONT, WHITE, screen, SCREEN_WIDTH // 2, 60)

        # Check game over condition
        if lives <= 0:
            draw_text("GAME OVER!", FONT, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

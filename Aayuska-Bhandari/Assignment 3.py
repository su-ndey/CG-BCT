
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player spaceship settings
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# Font for text
font = pygame.font.SysFont("Arial", 30)

# Clock
clock = pygame.time.Clock()

# Function to draw the player spaceship
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

# Function to draw bullets
def draw_bullets(bullets):
    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, bullet)

# Function to draw enemies
def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

# Function to check for collisions between bullets and enemies
def check_collision(bullets, enemies):
    global score
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

# Function to check if the player collides with any enemy
def check_player_collision(player_rect, enemies):
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            return True  # Player collided with an enemy
    return False

# Function to move the enemies
def move_enemies(enemies):
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

# Function to generate new enemies
def generate_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
    enemy_y = random.randint(-150, -50)
    return pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Function to display "Game Over"
def display_game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

# Main game loop
score = 0
game_over = False

while True:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_over:
        display_game_over()
        pygame.display.update()
        continue

    # Key press detection
    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Shoot bullet
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y, bullet_width, bullet_height)
        bullets.append(bullet)

    # Update bullet positions
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Generate new enemies
    if random.randint(1, 60) == 1:
        enemies.append(generate_enemy())

    # Move enemies
    move_enemies(enemies)

    # Check for bullet-enemy collisions
    check_collision(bullets, enemies)

    # Check for player-enemy collisions
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    if check_player_collision(player_rect, enemies):
        game_over = True

    # Draw the player
    draw_player(player_x, player_y)

    # Draw bullets
    draw_bullets(bullets)

    # Draw enemies
    draw_enemies(enemies)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Frame rate control
    clock.tick(60)

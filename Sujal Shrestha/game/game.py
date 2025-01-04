import pygame
import random
import math
import os  # For file handling
from pygame import mixer

# Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8
enemy_spawn_threshold = 5  # Increase enemies every 5 points
base_falling_speed = 40    # Initial falling speed
speed_increment = 1        # Speed increase per threshold
speed_threshold = 5        # Increase speed every 5 points

spawned_enemies = 0  # Track total spawned enemies

def spawn_enemy():
    """Adds a new enemy to the game."""
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(base_falling_speed)

for _ in range(num_of_enemies):
    spawn_enemy()

# Bullet
bulletImg = pygame.image.load('bullet.png')
bullets = []
bulletY_change = 3

# Score and High Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# High Score Handling
high_score_file = "high_score.txt"

# Load high score from file
if os.path.exists(high_score_file):
    with open(high_score_file, "r") as file:
        high_score = int(file.read())
else:
    high_score = 0

def save_high_score():
    """Save the high score to a file."""
    with open(high_score_file, "w") as file:
        file.write(str(high_score))

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    high_score_text = font.render("High Score : " + str(high_score), True, (255, 255, 255))
    screen.blit(score, (x, y))
    screen.blit(high_score_text, (x, y + 40))

def game_over_menu():
    """Display the Game Over menu with Restart and Quit options."""
    screen.fill((0, 0, 0))
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 150))

    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    quit_text = font.render("Press Q to Quit", True, (255, 255, 255))

    screen.blit(restart_text, (250, 300))
    screen.blit(quit_text, (250, 350))

    pygame.display.update()

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    """Fires 2 bullets from different positions."""
    offsets = [-20, 20]
    for offset in offsets:
        bullets.append({"x": x + 16 + offset, "y": y})

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 27

def update_bullets():
    """Update all bullets on screen."""
    global score_value, high_score
    for bullet in bullets[:]:
        bullet["y"] -= bulletY_change
        if bullet["y"] < 0:
            bullets.remove(bullet)
            continue

        for i in range(len(enemyX)):
            if isCollision(enemyX[i], enemyY[i], bullet["x"], bullet["y"]):
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bullets.remove(bullet)
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
                score_value += 1
                high_score = max(high_score, score_value)  # Update high score
                break

        screen.blit(bulletImg, (bullet["x"], bullet["y"]))

# Game Loop
def main_game():
    global playerX, playerY, playerX_change, score_value, bullets, enemyX, enemyY, enemyX_change, enemyY_change, spawned_enemies

    playerX = 370
    playerY = 480
    playerX_change = 0
    score_value = 0
    bullets = []
    
    enemyX.clear()
    enemyY.clear()
    enemyX_change.clear()
    enemyY_change.clear()

    for _ in range(num_of_enemies):
        spawn_enemy()

    running = True
    while running:

        # RGB Background
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score()  # Save high score when exiting
                running = False

            # Key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.6
                elif event.key == pygame.K_RIGHT:
                    playerX_change = 0.6
                elif event.key == pygame.K_SPACE:
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    fire_bullet(playerX, playerY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Player Movement
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(len(enemyX)):
            if enemyY[i] > 440:
                for j in range(len(enemyY)):
                    enemyY[j] = 2000
                save_high_score()  # Save high score at game over
                game_over_menu()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return True
                            if event.key == pygame.K_q:
                                pygame.quit()
                                exit()

            # Update enemy falling speed based on score
            enemyY_change[i] = base_falling_speed + (score_value // speed_threshold) * speed_increment

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.5
                enemyY[i] += enemyY_change[i]

            enemy(enemyX[i], enemyY[i], i)

        # Increase enemies dynamically
        if score_value // enemy_spawn_threshold > spawned_enemies:
            spawned_enemies += 1
            spawn_enemy()

        # Update Bullets
        update_bullets()

        # Draw Player and Score
        player(playerX, playerY)
        show_score(textX, textY)

        pygame.display.update()

while True:
    if not main_game():
        break

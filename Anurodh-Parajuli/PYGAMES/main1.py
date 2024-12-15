import random
import math
import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('749.jpg')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("ARCADE GAME")
icon = pygame.image.load('arcade-game.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('3d-rocket.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('icons8-alien-monster-emoji-48.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -1
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:  # Adjusted for better collision detection
        return True
    return False


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))


def game_over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (x, y))


# Game loop
running = True
game_over = False  # Variable to check if the game is over

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound('sound.wav')  # bullet_sound instead of bullet_Sound
                bullet_sound.play()
                bulletX = playerX  # Set bulletX when the spacebar is pressed
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if not game_over:
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        for i in range(num_of_enemies):
            if enemyY[i] > 300:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000  # Move all enemies off screen
                game_over_text(200, 250)
                game_over = True  # Set game over to True
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.3
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.3
                enemyY[i] += enemyY_change[i]

            if bullet_state == "fire" and isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.set_volume(0.5)
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY += bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)

    # After game over, stop the game until user input
    if game_over:
        game_over_text(200, 250)
        pygame.display.update()
        # Wait for user input to continue or quit
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Press Enter to restart
                        # Reset the game state
                        playerX = 370
                        playerY = 480
                        playerX_change = 0
                        score_value = 0
                        enemyX = [random.randint(0, 800) for _ in range(num_of_enemies)]
                        enemyY = [random.randint(50, 150) for _ in range(num_of_enemies)]
                        game_over = False
                        waiting_for_input = False
                    elif event.key == pygame.K_ESCAPE:  # Press ESC to quit
                        running = False
                        waiting_for_input = False

    pygame.display.update()


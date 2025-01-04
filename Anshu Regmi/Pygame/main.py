import pygame
import random
import math

from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(r'C:\Users\HP\Desktop\Pygame\ufo.jpg')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load(r'C:\Users\HP\Desktop\Pygame\background-image.png')

#background sound
mixer.music.load(r'C:\Users\HP\Desktop\Pygame\background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load(r'C:\Users\HP\Desktop\Pygame\space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Monsters
monsterImg = []
monsterX = []
monsterY = []
monsterX_change = []
monsterY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    monsterImg.append(pygame.image.load(r'C:\Users\HP\Desktop\Pygame\monster.png'))
    monsterX.append(random.randint(0, 735))
    monsterY.append(random.randint(50, 150))
    monsterX_change.append(3)  # Adjust speed as needed
    monsterY_change.append(40)

# Bullet
bulletImg = pygame.image.load(r'C:\Users\HP\Desktop\Pygame\Bullet-1.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"
bullet_sound=mixer.Sound(r'C:\Users\HP\Desktop\Pygame\laser.wav')
bullet_sound.play()

# Initial score
ini_score = 0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
    score=font.render("Score:"+str(ini_score),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def monster(x, y, i):
    screen.blit(monsterImg[i], (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(monsterX, monsterY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - monsterX, 2) + math.pow(bulletY - monsterY, 2))
    return distance < 27

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update player position
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Monster movement and collision detection
    for i in range(no_of_enemies):
        monsterX[i] += monsterX_change[i]

        # Reverse direction on hitting screen boundaries
        if monsterX[i] <= 0:
            monsterX_change[i] = 1
            monsterY[i] += monsterY_change[i]
        elif monsterX[i] >= 736:
            monsterX_change[i] = -3
            monsterY[i] += monsterY_change[i]

        # Check collision
        collision = is_collision(monsterX[i], monsterY[i], bulletX, bulletY)
        if collision:
            explosion_sound=mixer.Sound(r'C:\Users\HP\Desktop\Pygame\explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            ini_score += 1
            print(f"Score: {ini_score}")
            monsterX[i] = random.randint(0, 735)
            monsterY[i] = random.randint(50, 150)

        # Draw the monster
        monster(monsterX[i], monsterY[i], i)

    # Draw the player
    player(playerX, playerY)
    show_score(textX,textY)
    # Update the display
    pygame.display.update()


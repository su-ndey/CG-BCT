import pygame
from pygame import mixer
import random
import math

# Initializing PyGame
pygame.init()
mixer.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

# Setting Display Dimensions
screen = pygame.display.set_mode((850, 600))

# Changing Window Title
pygame.display.set_caption("   Space Invader")

# Setting Window Icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Loading Img
background = pygame.image.load('bg.png')
playerimg = pygame.image.load('arcade.png')
enemyimg = pygame.image.load('enemy.png')
bulletimg = pygame.image.load('bullet.png')

# Creating Many Aliens
enemyimg = []
enemyX = []
enemyY = []
enemyspeedX = []
enemyspeedY = []
no_of_aliens = 7

for i in range(no_of_aliens):
    enemyimg.append(pygame.image.load('enemy.png'))
    # Axis Of Enemy At Random Positions
    enemyX.append(random.randint(0, 786))
    enemyY.append(random.randint(30, 200))
    # Speed Of Enemy
    enemyspeedX.append(-10)
    enemyspeedY.append(40)

# Axis Of Player
playerX = 425
playerY = 510
changeX = 0

# Bullet Fire
check = False
bulletX = 441
bulletY = 475

# To Show Score Or Total Enemy Killed
score = 0 
score_font = pygame.font.SysFont('Candara', 27, 'bold')
def score_text():
    score_img = score_font.render('Score:{}'.format(score), True, 'white')
    screen.blit(score_img, (10, 10))

# To Show Game Over On Screen
gameover_font = pygame.font.SysFont('Candara', 64, 'bold')
def gamover():
    gameover_img = gameover_font.render('Gamover Over', True, 'white')
    screen.blit(gameover_img, (200, 255))

# Screen On Hold
running = True
while running: # If Only Used True Boolean Than Window Will Be In Infinite Loop.

    # Drawing BackGround Img In Window
    screen.blit(background, (0, 0))

    # For Closing Window Using Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Changing Axis Of Player
        if event.type == pygame.KEYDOWN:
            # Can Increase The Speed Of Player
            if event.key == pygame.K_LEFT:
                changeX =- 7 # playerX = playerX - changeX
            if event.key == pygame.K_RIGHT:
                changeX = 7 # playerX = playerX + changeX
            if event.key == pygame.K_SPACE:
                if check == False:
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    check = True
                    bulletX = playerX + 16
        if event.type == pygame.KEYUP:
            changeX = 0

    playerX += changeX # playerX = playerX + (-changeX) or playerX = playerX + changeX

    # Not Letting Player Go Out Of The Window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 785:
        playerX = 785

    for i in range(no_of_aliens):
        screen.blit(enemyimg[i], (enemyX[i], enemyY[i]))
        enemyX[i] += enemyspeedX[i]
        # Making Enemy Go Left To Right When It Touches 0 X-Axis Or 785 Y-Axis
        if enemyX[i] <= 0:
            enemyspeedX[i] = 10
            # Making Enemy Go Down By 10px When It Touches 0 X-Axis
            enemyY[i] += enemyspeedY[i]
        elif enemyX[i] >= 785:
            enemyspeedX[i] -= 10
            # Making Enemy Go Down By 10px When It Touches 785 X-Axis
            enemyY[i] += enemyspeedY[i]

        # Collision Betn Enemy And Bullet
        d = math.sqrt(math.pow((bulletX - enemyX[i]), 2) + math.pow((bulletY - enemyY[i]), 2))
        # print(d)
        if d < 36:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 475
            check = False
            # Make Enemy Go Back To It's Orignal Position
            enemyX[i] = random.randint(0, 786)
            enemyY[i] = random.randint(30, 200)
            score += 1
            # print(score)
        # Will Show Game Over On Screen
        if enemyY[i] > 422:
            for j in range(no_of_aliens):
                enemyY[j] = 2000
            score_text()
            gamover()
            break

    # bulletY -= 3
    # Not Letting Bullet Img Out Of The Window And Firing Bullet Only Once
    if bulletY <= 0:
        bulletY = 473
        check = False

    # Drawing Images On Window
    if check == True:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= 6

    score_text()
    screen.blit(playerimg, (playerX, playerY))

    # Updating Window
    pygame.display.update()

# print("Hello, World!")

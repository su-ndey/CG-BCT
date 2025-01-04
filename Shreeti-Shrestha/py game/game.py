import math
import random
import pygame
from pygame import mixer

pygame.init()  # Pygame is initialized

screen = pygame.display.set_mode((800, 600))  # Screen is created
background = pygame.image.load(r'C:\Users\Lenovo\Desktop\Shreeti Shrestha\CG-BCT\Shreeti-Shrestha\py game\background.png')

# Background Noise
mixer.music.load("c:/Users/Lenovo/Desktop/Shreeti Shrestha/CG-BCT/Shreeti-Shrestha/py game/background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(r'C:\Users\Lenovo\Desktop\Shreeti Shrestha\CG-BCT\Shreeti-Shrestha\py game\001-ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(r'C:\Users\Lenovo\Desktop\Shreeti Shrestha\CG-BCT\Shreeti-Shrestha\py game\player.png')
playerX = 100 #for position of the player during initial
playerY = 480
playerY_change = 0  #initially their is no position change
playerX_change = 0  

# Enemy(list are created for multiple enemies and are displayed one by one but looks to be appearing simultaniously)
enemyImg = []
enemyX = []  
enemyY = []
enemyX_change = []  
enemyY_change = []  
num_of_enemies = 6

#for loop is to add values to the list from append 
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r'C:\Users\Lenovo\Desktop\Shreeti Shrestha\CG-BCT\Shreeti-Shrestha\py game\enemy.png'))
    enemyX.append(random.randint(750, 800))  
    enemyY.append(random.randint(50, 150)) 
    enemyX_change.append(random.uniform(-0.05, -0.1))  
    enemyY_change.append(random.choice([1, 2]))  

# Bullet
bulletImg = pygame.image.load(r'C:\Users\Lenovo\Desktop\Shreeti Shrestha\CG-BCT\Shreeti-Shrestha\py game\bullet.png')
bulletX = 0 
bulletY = 480
bulletX_change = 0  
bulletY_change = 0  
bullet_state = "ready"  # Ready means the bullet is not moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means to draw

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y, direction):
    global bullet_state, bulletX, bulletY, bulletX_change
    bullet_state = "fire"
    bulletX_change = direction  # horizontal direction
    screen.blit(bulletImg, (x + 50, y + 0.1  ))  # to adjust bullet's position

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))) #distance measure formula
    if distance < 27:  
        return True
    return False

def isPlayerCollision(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt((math.pow(playerX - enemyX, 2)) + (math.pow(playerY - enemyY, 2)))
    if distance < 50:  
        return True
    return False

def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (250, 250))

# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it's up or down, right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -1 
            if event.key == pygame.K_DOWN:
                playerY_change = 1  
            if event.key == pygame.K_LEFT:
                playerX_change = -1  
            if event.key == pygame.K_RIGHT:
                playerX_change =  1  
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound(r'c:/Users/Lenovo/Desktop/Shreeti Shrestha/CG-BCT/Shreeti-Shrestha/py game/laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX #aligns players position with the 
                    bulletY = playerY 
                    fire_bullet(bulletX, bulletY, 5)  # fires the bullet
                    
        # once the key is released, the movement is stoped 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  

    # Update player's position 
    playerX += playerX_change
    playerY += playerY_change

    # Boundary conditions for player
    # vertical
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536 

    # horizontal
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: 
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]  # Move from right to left with randomized speed
        enemyY[i] += enemyY_change[i]  # vertical movement
 
        if enemyY[i] <= 50 or enemyY[i] >= 536:
            enemyY_change[i] *= -1  # Reverse vertical movement direction

        # player-enemy collision to end the game
        if isPlayerCollision(playerX, playerY, enemyX[i], enemyY[i]):
            game_over()  # Displays game over message
            running = False  # Ends the game loop

        # Collision with bullet
        if bullet_state == "fire":  # Checks if the bullet is fired
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480  # Resets the bullet
                bullet_state = "ready"
                score_value += 1  # Increases score
                enemyX[i] = random.randint(750, 800)  # Resets enemy to the right side of the screen
                enemyY[i] = random.randint(50, 150)  # Resets enemy's Y position
           

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        bulletX += bulletX_change  # Moves bullet horizontally
        screen.blit(bulletImg, (bulletX + 50, bulletY + 0.1))  # Draws bullet at new position

        # Reset bullet
        if bulletX <= 0 or bulletX >= 800:
            bullet_state = "ready"
            bulletX = 0 

    player(playerX, playerY)
    show_score(10,10) #score to appear on the screen
    pygame.display.update() 
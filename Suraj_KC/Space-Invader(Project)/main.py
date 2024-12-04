import pygame as pg

import random

pg.init()
screen = pg.display.set_mode((960,540))

background_music = pg.mixer.music.load("./sound/background.wav")
pg.mixer.music.play(-1)
pg.display.set_caption("Space Invaders")
icon = pg.image.load('./icon/ufo.png')
pg.display.set_icon(icon)

background = pg.image.load('./icon/bg.jpg')


playerImg = pg.image.load('./icon/spaceship.png')


playerX = 444
playerY = 432
playerX_change = 0

enemyImg =[]
enemyX = []
enemyY= []
enemyX_change =[]
enemyY_change=[]



def enemy_position():
    global enemyX,enemyY,enemyX_change,enemyY_change
    enemyImg.append(pg.image.load('./icon/alien.png'))
    enemyX.append(random.randint(0,898))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(40)

def enemy_reset(no_of_enemies,i):
    global enemyX,enemyY,enemyX_change,enemyY_change
    enemyX[i] = random.randint(0,898)
    enemyY[i] = random.randint(50,150)
    enemyX_change[i] = 1
    enemyY_change[i] = 40
    
no_of_enemies = 6

for i in range(no_of_enemies):
    enemy_position()

bulletImg = pg.image.load('./icon/1bullet.png')
bulletX = 0
bulletY = 420
bulletY_change  =2
bullet_state = "ready"

score_value = 0
font = pg.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

game_over_font = pg.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    score = font.render(f"Score : {str(score_value)}",True,(255,255,255))
    screen.blit(score,(x,y))

def game_over():
    text =  game_over_font.render(f" GAME       OVER",True,(255,255,255))
    screen.blit(text,(200,220))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(enemyImg,x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = ((bulletX-enemyX)**2 + (bulletY-enemyY)**2)**0.5
    if distance < 27:
        return True
    return False


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            running  =False

        if (event.type == pg.KEYDOWN):
            if (event.key == pg.K_LEFT or event.key == pg.K_a):
                playerX_change= -2
                print("Left movement is done")
            if (event.key ==pg.K_RIGHT or event.key == pg.K_d):
                playerX_change= 2
                print("Right movement is done")

            if (event.key ==pg.K_SPACE and bullet_state is "ready"):
                bullet_sound = pg.mixer.Sound("./sound/laser.wav")
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX,bulletY)
            
        if (event.type == pg.KEYUP):
            if (event.key == pg.K_LEFT or event.key == pg.K_a) or (event.key ==pg.K_RIGHT or event.key == pg.K_d):
                playerX_change=0
                print("Keystorke released")
        
    playerX += playerX_change
    if (playerX >= 896):
        playerX = 896        
    elif (playerX <=0):
        playerX = 0
    for i in range(no_of_enemies):
        if enemyY[i] >340:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over()
            break 
        enemyX[i] += enemyX_change[i]  
        if (enemyX[i] >= 896):
                enemyX_change[i] =-1
                enemyY[i] += enemyY_change[i]      
        elif (enemyX[i] <=0):
                enemyX_change[i] = 1
                enemyY[i] +=  enemyY_change[i]
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_sound = pg.mixer.Sound("./sound/explosion.wav")
            collision_sound.play()
            bulletY = 420
            bullet_state = "ready"
            score_value += 5
            
            enemy_reset(no_of_enemies,i)
        enemy(enemyImg[i],enemyX[i],enemyY[i]) 
    if (bulletY <0):
        bulletY = 420
        bullet_state = "ready"
    if (bullet_state is "fire"):
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change
    
        
    
    player(playerX,playerY)
    show_score(textX,textY)
    
    pg.display.update()
    


    
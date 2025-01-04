import pygame
import time
from random import randint

black = (0, 0, 0)
textcolor1 = (255, 32, 23)
textcolor2 = (235, 32, 55)
textcolorBlock = (0, 0, 235)
sunset = (255, 0, 0)
green = (100, 255, 100)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()

img = pygame.image.load("bird.png")
background = pygame.image.load("background1.jpg")
imageWidth = img.get_width()
imageHeight = img.get_height()

def score(count, level):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    score = "score: " + str(count) + "   level:" + str(level)
    titleTextSurface, titleTextRectangle = makeTextObjs(score, smallText, sunset)
    titleTextRectangle.center = surfaceWidth / 2, 20
    surface.blit(titleTextSurface, titleTextRectangle)

def blocks(x_block, y_block, blockWidth, blockHeight, gap, color):
    pygame.draw.rect(surface, color, [x_block, y_block, blockWidth, blockHeight])
    pygame.draw.rect(surface, color, [x_block, y_block + blockHeight + gap, blockWidth, surfaceHeight - gap - blockHeight])
    pygame.draw.rect(surface, textcolorBlock, [x_block - 5, blockHeight - 10, blockWidth + 10, 30])
    pygame.draw.rect(surface, textcolorBlock, [x_block - 5, y_block + blockHeight + gap, blockWidth + 10, 30])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def msgsurface(text):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    largeText = pygame.font.Font("freesansbold.ttf", 50)

    titleTextSurface, titleTextRectangle = makeTextObjs(text, largeText, textcolor1)
    titleTextRectangle.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurface, titleTextRectangle)

    smallTextSurface, smallTextRectangle = makeTextObjs("Press any key to continue", smallText, textcolor2)
    smallTextRectangle.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)

    hscore = open("score.log", 'r')
    high_score = hscore.read()
    hscore.close()

    highscoresurface, highscoreRectangle = makeTextObjs("Highscore: " + high_score, smallText, textcolor2)
    highscoreRectangle.center = surfaceWidth / 2, ((surfaceHeight / 2) + 150)

    surface.blit(smallTextSurface, smallTextRectangle)
    surface.blit(highscoresurface, highscoreRectangle)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()
    main()

def gameOver(finalscore):
    hscore = open("score.log", 'r')
    high_score = hscore.read()
    hscore.close()
    if high_score == "" or (int(high_score) < int(finalscore)):
        writescore = open("score.log", "w")
        writescore.write(str(finalscore))
        writescore.close()
    msgsurface("Game Over")

def gameStart():
    try:
        hscore = open("score.log", 'r')
        high_score = hscore.read()
        hscore.close()
    except:
        writescore = open("score.log", "w")
        writescore.write(str(0))
        writescore.close()
    msgsurface("Press Up arrow to move the bird")

def image(x, y, img):
    surface.blit(img, (x, y))

def main():
    x = 200
    y = 150
    y_move = 0

    x_block = surfaceWidth
    y_block = 0
    blockWidth = 80
    blockHeight1 = randint(100, int(surfaceHeight / 1.5) - 100)

    current_score = 0
    i = 1
    level = 0

    gap = int(imageHeight * 4)
    block_move = 4

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 4

        y += y_move

        image(0, 0, background)
        image(x, y, img)

        blocks(x_block, y_block, blockWidth, blockHeight1, gap, green)
        x_block -= block_move

        score(current_score, level)

        if y > surfaceHeight - imageHeight or y < 0:
            gameOver(current_score)

        if x_block < (-1 * blockWidth):
            x_block = surfaceWidth
            blockHeight1 = randint(0, int(surfaceHeight / 1.5))

        if x + imageWidth > x_block:
            if x < x_block + blockWidth:
                if y < blockHeight1 + 15:
                    gameOver(current_score)

        if x + imageWidth > x_block:
            if y + imageHeight > blockHeight1 + gap:
                if x < x_block + blockWidth:
                    gameOver(current_score)

        if x < x_block + 40 and x > x_block - block_move + i * 20:
            current_score += 1

        if 20 <= current_score < 40:
            block_move = 8
            if x_block < (-.99 * blockWidth):
                gap = int(imageHeight * 3)
                level = "I"

        if 40 <= current_score < 60:
            block_move = 10
            if x_block < (-.99 * blockWidth):
                gap = int(imageHeight * 2.5)
                level = "II"

        if 60 <= current_score < 100:
            block_move = 11
            if x_block < (-.99 * blockWidth):
                gap = int(imageHeight * 2)
                level = "IV"

        if current_score > 100:
            block_move = 12
            level = "V"

        pygame.display.update()
        clock.tick(60)

gameStart()
main()
pygame.quit()
quit()

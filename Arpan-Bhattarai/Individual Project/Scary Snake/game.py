import pygame
import random
import os
pygame.init()
pygame.mixer.init()

#Game Window
gameWindow = pygame.display.set_mode((900, 600))

#Game Title
pygame.display.set_caption("Scary Snake")
pygame.display.update()

#backgroundImage
bg_img = pygame.image.load("background image.png").convert_alpha()
bg_img = pygame.transform.scale(bg_img, (900, 600))

welc_img = pygame.image.load("welcomescreen.png").convert_alpha()
welc_img = pygame.transform.scale(welc_img, (900, 600))

gover_img = pygame.image.load("gameover.png").convert_alpha()
gover_img = pygame.transform.scale(gover_img, (900, 600))

beep_sound = pygame.mixer.Sound('beep.wav')

clock = pygame.time.Clock()

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


font = pygame.font.SysFont("comicsans", 30)
def text_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(welc_img, (0, 0))
        ##text_on_screen("Welcome to Scary Snakes", blue, 260, 240)
        ##text_on_screen("Press Space to Play", red, 300, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bgm.mp3')
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(60)



#Game loop
def game_loop():
    #Game Variables
    exit_game = False
    game_over = False
    snake_x = 430
    snake_y = 270
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    score = 0
    food_x = random.randint(0, 600)
    food_y = random.randint(0, 300)
    snake_list = []
    snake_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write(str("0"))
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(gover_img, (0, 0))
            ##text_on_screen("Game Over! Press enter to continue", red, 200, 240)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y =  - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score = score + 10
                food_x = random.randint(0, 600)
                food_y = random.randint(0, 300)
                snake_length = snake_length + 5
                beep_sound.play()
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bg_img, (0,0))
            head = [snake_x, snake_y]
            snake_list.append(head)
            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.draw.rect(gameWindow, red, (food_x, food_y, snake_size, snake_size))
            text_on_screen("Score: " + str(score) + "  Highscore: " + str(highscore), black, 5, 5)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Gameover.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > 900 or snake_y < 0 or snake_y > 600:
                game_over = True
                pygame.mixer.music.load('Gameover.mp3')
                pygame.mixer.music.play()


        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()

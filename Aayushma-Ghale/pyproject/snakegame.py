import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Game settings
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)

# FPS (Frames per second)
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 5

# Load images
snake_head_img = pygame.image.load('snake.png')  # Replace with your image file
snake_head_img = pygame.transform.scale(snake_head_img, (snake_block, snake_block))  # Scale to 20x20


food_img = pygame.image.load('apple.png')  # Replace with your image file
food_img = pygame.transform.scale(food_img, (snake_block, snake_block))  # Scale to 20x20

# Optional: Background image
background_img = pygame.image.load('background.png')  # Replace with your image file
background_img = pygame.transform.scale(background_img, (width, height))  # Scale to fit the screen

# Load sounds
eat_sound = pygame.mixer.Sound('bite.mp3')  # Make sure you have the sound file
collision_sound = pygame.mixer.Sound('gameover.mp3')  # Make sure you have the sound file

# Font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Game over function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Score function
def score_display(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    screen.blit(value, [0, 0])

# Snake function
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        if x == snake_list[0]:
            screen.blit(snake_head_img, (x[0], x[1]))  # Snake head
        else:
            screen.blit(snake_head_img, (x[0], x[1]))  # Snake body part (using head image for simplicity)

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake starting position
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            score_display(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            collision_sound.play()  # Play collision sound
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        
        # Draw the background
        screen.blit(background_img, (0, 0))  # Draw background image
        screen.blit(food_img, (foodx, foody))  # Food image

        # Snake movement and body
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                collision_sound.play()  # Play collision sound
                game_close = True

        draw_snake(snake_block, snake_List)
        score_display(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            eat_sound.play()  # Play eat sound
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()

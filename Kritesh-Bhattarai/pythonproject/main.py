import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooting Game")

# Load and resize images
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (50, 50))

enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Load power-up images
shield_img = pygame.image.load("shield.png")
shield_img = pygame.transform.scale(shield_img, (30, 30))

# Load sounds
bullet_sound = pygame.mixer.Sound("laser.wav")
game_over_sound = pygame.mixer.Sound("game_over.mp3")
pygame.mixer.music.load("background.mp3")  # Load background music

# Player settings
player_pos = [screen_width // 2, screen_height - 60]
player_speed = 5

# Bullet settings
bullets = []
bullet_speed = 7
bullet_firing_rate = 300  # milliseconds
last_bullet_fired = pygame.time.get_ticks()

# Enemy settings
enemies = []
enemy_speed = 2
enemy_spawn_time = 1000  # milliseconds
last_enemy_spawn = pygame.time.get_ticks()

# Power-up settings
power_ups = []

# Shield settings
shield_active = False
shield_start_time = 0
shield_duration = 10000  # 10 seconds

# Score
score = 0
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

# Game states
PLAYING = 0
GAME_OVER = 1
WAITING_TO_START = 2
game_state = WAITING_TO_START

def reset_game():
    global player_pos, bullets, enemies, last_enemy_spawn, game_state, score, power_ups, shield_active, shield_start_time
    player_pos = [screen_width // 2, screen_height - 60]
    bullets = []
    enemies = []
    power_ups = []
    last_enemy_spawn = pygame.time.get_ticks()
    score = 0
    shield_active = False
    shield_start_time = 0
    game_state = PLAYING

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

class PowerUp:
    def __init__(self, x, y, img, effect):
        self.x = x
        self.y = y
        self.img = img
        self.effect = effect
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.y += 5  # Move power-up down the screen
        self.rect.topleft = (self.x, self.y)

    def off_screen(self):
        return self.y > screen_height

    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 10000  # 10 seconds

# Function to spawn power-ups
def spawn_power_up():
    # Check if there is already a shield power-up on the screen
    if random.randint(0, 1000) < 5:  # 0.5% chance to spawn a power-up
        if not any(pu.effect == "shield" for pu in power_ups):  # Prevent multiple shields
            x = random.randint(0, screen_width - 30)
            y = -30
            power_ups.append(PowerUp(x, y, shield_img, "shield"))

# Main game loop
running = True
space_pressed = False
pygame.mixer.music.play(-1)  # Play background music in a loop
while running:
    dt = clock.tick(60)  # Frame rate

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == WAITING_TO_START:
                reset_game()
                pygame.mixer.music.stop()  # Stop background music when game starts
            elif game_state == GAME_OVER and event.key == pygame.K_RETURN:
                game_state = WAITING_TO_START
                pygame.mixer.music.play(-1)  # Play background music again
            elif game_state == PLAYING and event.key == pygame.K_SPACE:
                space_pressed = True
                bullet_sound.play()
        if event.type == pygame.KEYUP:
            if game_state == PLAYING and event.key == pygame.K_SPACE:
                space_pressed = False
                bullet_sound.stop()

    if game_state == PLAYING:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_img.get_width():
            player_pos[0] += player_speed

        # Bullet firing
        current_time = pygame.time.get_ticks()
        if space_pressed and current_time - last_bullet_fired > bullet_firing_rate:
            bullets.append([player_pos[0] + player_img.get_width() // 2, player_pos[1]])
            last_bullet_fired = current_time

        # Bullet movement
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Enemy spawning
        if current_time - last_enemy_spawn > enemy_spawn_time:
            enemy_x = random.randint(0, screen_width - enemy_img.get_width())
            enemies.append([enemy_x, 0])
            last_enemy_spawn = current_time

        # Enemy movement
        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            if enemy[1] > screen_height:
                game_state = GAME_OVER
                pygame.mixer.stop()  # Stop all sounds
                game_over_sound.play()
                break

        # Bullet-enemy collision detection
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if enemy[0] < bullet[0] < enemy[0] + enemy_img.get_width() and enemy[1] < bullet[1] < enemy[1] + enemy_img.get_height():
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        # Player-enemy collision detection
        for enemy in enemies[:]:
            if player_pos[0] < enemy[0] + enemy_img.get_width() and player_pos[0] + player_img.get_width() > enemy[0] and player_pos[1] < enemy[1] + enemy_img.get_height() and player_pos[1] + player_img.get_height() > enemy[1]:
                if not shield_active:
                    game_state = GAME_OVER
                    pygame.mixer.stop()  # Stop all sounds
                    game_over_sound.play()
                    break

        # Spawn power-ups
        spawn_power_up()

        # Update power-ups
        for power_up in power_ups[:]:
            power_up.update()
            # Remove off-screen or expired power-ups
            if power_up.off_screen() or power_up.expired():
                power_ups.remove(power_up)

        # Check for collisions with power-ups
        for power_up in power_ups[:]:
            if player_pos[0] < power_up.rect.x + power_up.rect.width and player_pos[0] + player_img.get_width() > power_up.rect.x and player_pos[1] < power_up.rect.y + power_up.rect.height and player_pos[1] + player_img.get_height() > power_up.rect.y:
                if power_up.effect == "shield":
                    shield_active = True
                    shield_start_time = pygame.time.get_ticks()
                power_ups.remove(power_up)

        # Update shield timer
        if shield_active and pygame.time.get_ticks() - shield_start_time > shield_duration:
            shield_active = False

    # Drawing
    screen.blit(background_img, (0, 0))  # Draw background image
    if game_state == PLAYING:
        screen.blit(player_img, player_pos)
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for enemy in enemies:
            screen.blit(enemy_img, enemy)
        for power_up in power_ups:
            power_up.draw(screen)
        draw_text(f"Score: {score}", font, (255, 255, 255), screen, 70, 20)
        if shield_active:
            remaining_time = (shield_duration - (pygame.time.get_ticks() - shield_start_time)) // 1000
            draw_text(f"Shield: {remaining_time}s", font, (255, 255, 255), screen, screen_width - 100, 20)
    elif game_state == GAME_OVER:
        draw_text("Game Over", pygame.font.Font(None, 74), (255, 0, 0), screen, screen_width // 2, screen_height // 2)
        draw_text(f"Final Score: {score}", pygame.font.Font(None, 36), (255, 255, 255), screen, screen_width // 2, screen_height // 2 + 50)
        draw_text("Press Enter to Restart", pygame.font.Font(None, 36), (255, 255, 255), screen, screen_width // 2, screen_height // 2 + 100)
    elif game_state == WAITING_TO_START:
        draw_text("Press Any Key to Start", pygame.font.Font(None, 36), (255, 255, 255), screen, screen_width // 2, screen_height // 2)

    pygame.display.flip()

pygame.quit()

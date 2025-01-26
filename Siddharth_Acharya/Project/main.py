import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 60, 30  # Set the desired car width and height

# Colors
WHITE = (255, 255, 255)

# Load background image
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize to fit screen

# Load car images and resize them
car_images = [pygame.transform.scale(pygame.image.load(f'car{i}.png'), (CAR_WIDTH, CAR_HEIGHT)) for i in range(1, 7)]

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Crossing Zombie")

# Clock to control frame rate
clock = pygame.time.Clock()

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Zombie color (green)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, lane, speed):
        super().__init__()
        self.image = random.choice(car_images)  # Randomly select a car image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH  # Start vehicles from the right side of the screen
        self.rect.y = lane
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed  # Move vehicles to the left
        if self.rect.x + self.rect.width < 0:  # Reset position when vehicle leaves screen
            self.rect.x = WIDTH
            self.rect.y = random.randint(100, 400)  # Randomize lane again

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        self.image = pygame.Surface((30, 30))
        if type == "health":
            self.image.fill((0, 255, 255))  # Health pack (cyan)
        elif type == "speed":
            self.image.fill((255, 255, 0))  # Speed boost (yellow)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Scroll down to simulate falling power-ups
        self.rect.y += 2
        if self.rect.y > HEIGHT:
            self.kill()  # Remove from the game when it goes off-screen


def check_collisions(zombie, vehicles, powerups):
    if pygame.sprite.spritecollide(zombie, vehicles, False):
        return True  # Game Over (Zombie hit a vehicle)
    for powerup in powerups:
        if pygame.sprite.collide_rect(zombie, powerup):
            return powerup.type  # Return power-up type collected
    return None

def main():
    zombie = Zombie()
    all_sprites = pygame.sprite.Group(zombie)
    vehicles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    score = 0
    level = 1

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)
        
        # Draw background image
        screen.blit(background, (0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get user input
        keys = pygame.key.get_pressed()

        # Manually update the zombie sprite with keys
        zombie.update(keys)

        # Add vehicles and power-ups dynamically
        if random.random() < 0.02:  # Random chance to spawn vehicles
            lane = random.randint(100, 400)
            speed = random.randint(3, 6)
            vehicle = Vehicle(lane, speed)
            vehicles.add(vehicle)
            all_sprites.add(vehicle)

        if random.random() < 0.01:  # Random chance for power-up
            powerup = PowerUp(random.choice([100, 300, 500, 700]), 0, random.choice(["health", "speed"]))
            powerups.add(powerup)
            all_sprites.add(powerup)

        # Update all other sprites (not the zombie)
        for vehicle in vehicles:
            vehicle.update()
        for powerup in powerups:
            powerup.update()

        # Check collisions
        collision_result = check_collisions(zombie, vehicles, powerups)
        if collision_result == True:
            print("Game Over!")
            running = False
        elif collision_result == "health":
            score += 10
        elif collision_result == "speed":
            zombie.speed += 2

        # Draw everything
        all_sprites.draw(screen)

        # Display score at the top
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Set frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

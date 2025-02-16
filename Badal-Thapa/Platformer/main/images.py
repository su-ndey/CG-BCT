# Import the load_player_sprites function from the image_loader module
from image_loader import load_player_sprites
# Import the pygame library for game development
import pygame
# Import the join function from the os.path module to handle file paths
from os.path import join

# Load player walking animation sprites from the specified directory
PLAYER_WALK = load_player_sprites(
    join("main", "assets", "player", "walk-run", "normal", "walk"), 2)
# Load player running animation sprites from the specified directory
PLAYER_RUN = load_player_sprites(
    join("main", "assets", "player", "walk-run", "normal", "run"), 2)
# Load player jumping animation sprites from the specified directory
PLAYER_JUMP = load_player_sprites(
    join("main", "assets", "player", "walk-run", "normal", "jump"), 2)
# Load player pushing animation sprites from the specified directory
PLAYER_PUSH = load_player_sprites(
    join("main", "assets", "player", "walk-run", "normal", "push"), 2)
# Load player standing animation sprites from the specified directory
PLAYER_STAND = load_player_sprites(
    join("main", "assets", "player", "walk-run", "normal", "stand"), 2)
# Load player falling animation sprites from the specified directory
PLAYER_FALLING = load_player_sprites(
    join("main", "assets", "player", "walk-run", "normal", "falling"), 2)

# Load player walking animation sprites with a weapon from the specified directory
PLAYER_WALK_WEAPON = load_player_sprites(
    join("main", "assets", "player", "walk-run", "weapon", "walk_weapon"), 2)
# Load player running animation sprites with a weapon from the specified directory
PLAYER_RUN_WEAPON = load_player_sprites(
    join("main", "assets", "player", "walk-run", "weapon", "run_weapon"), 2)
# Load player jumping animation sprites with a weapon from the specified directory
PLAYER_JUMP_WEAPON = load_player_sprites(
    join("main", "assets", "player", "walk-run", "weapon", "jump_weapon"), 2)
# Load player pushing animation sprites with a weapon from the specified directory
PLAYER_PUSH_WEAPON = load_player_sprites(
    join("main", "assets", "player", "walk-run", "weapon", "push_weapon"), 2)
# Load player standing animation sprites with a weapon from the specified directory
PLAYER_STAND_WEAPON = load_player_sprites(
    join("main", "assets", "player", "walk-run", "weapon", "stand_weapon"), 2)
# Load player falling animation sprites with a weapon from the specified directory
PLAYER_FALLING_WEAPON = load_player_sprites(
    join("main", "assets", "player", "walk-run", "weapon", "falling_weapon"), 2)

# Load player attack (chop) animation sprites from the specified directory
PLAYER_ATTACK_CHOP = load_player_sprites(
    join("main", "assets", "player", "attack", "chop"), 2)

# Load the background image and scale it to 1.5 times its original size
BACKGROUND = pygame.image.load(join("main", "assets", "background.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (round(BACKGROUND.get_width() * 1.5), round(BACKGROUND.get_height() * 1.5)))

# Load the crate image
CRATE = pygame.image.load("main\\assets\\crate.png")
# Create a smaller version of the crate image (25% of the original size)
SMALL_CRATE = pygame.transform.scale(
    CRATE, (round(CRATE.get_width() * 0.25), round(CRATE.get_height() * 0.25)))
# Create a medium-sized version of the crate image (75% of the original size)
CRATE = pygame.transform.scale(
    CRATE, (round(CRATE.get_width() * 0.75), round(CRATE.get_height() * 0.75)))

# Load the door image and scale it to 25% of its original size
DOOR = pygame.image.load(join("main", "assets", "door.png"))
DOOR = pygame.transform.scale(DOOR, (round(DOOR.get_width() * 0.25), round(DOOR.get_height() * 0.25)))

# Load the platform image and scale it to 60% width and 30% height of its original size
PLATFORM = pygame.image.load(join("main", "assets", "platform.png"))
PLATFORM = pygame.transform.scale(PLATFORM, (round(PLATFORM.get_width() * 0.6), round(PLATFORM.get_height() * 0.3)))

# Load the spike image and scale it to 50% of its original size
SPIKE = pygame.image.load(join("main", "assets", "spike.png"))
SPIKE = pygame.transform.scale(SPIKE, (round(SPIKE.get_width() * 0.5), round(SPIKE.get_height() * 0.5)))

# Load a list of trampoline animation frames
TRAMPONLINE = [
    pygame.image.load(join("main", "assets", "jump", "jump1.png")),
    pygame.image.load(join("main", "assets", "jump", "jump2.png")),
    pygame.image.load(join("main", "assets", "jump", "jump3.png"))
]

# Load a list of coin animation frames
COIN = [
    pygame.image.load(join("main", "assets", "coin", "coin1.png")),
    pygame.image.load(join("main", "assets", "coin", "coin2.png")),
    pygame.image.load(join("main", "assets", "coin", "coin3.png"))
]

# Load the second dead animation frame and scale it to 2x its original size
DEAD2 = pygame.image.load(join("main", "assets", "player", "dead", "dead2.png"))
DEAD2 = pygame.transform.scale(DEAD2, (round(DEAD2.get_width() * 2), round(DEAD2.get_height() * 2)))

# Set the DEAD variable to the scaled DEAD2 image
DEAD = DEAD2

# Initialize an empty list to store block images
BLOCKS = []

# Loop through block images (1 to 11) and load them into the BLOCKS list
for i in range(1, 12):
    # Construct the file path for each block image
    file_path = join("main", "assets", "blocks", f"block{i}.png")
    # Load the block image
    image = pygame.image.load(file_path)
    # Scale the block image to 25% of its original size
    image = pygame.transform.scale(image, (image.get_width() // 4, image.get_height() // 4))
    # Add the scaled block image to the BLOCKS list
    BLOCKS.append(image)
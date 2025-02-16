# import pygame
# import json
# pygame.init()
# pygame.font.init()

# # GAME INFORMATION
# TITLE = "Hugo The Huge"
# MAX_FPS = 60

# # WINDOW
# WIDTH, HEIGHT = 1000, 700
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption(TITLE)

# from images import *
# from player import Player
# from block import Block
# from crate import Crate, SmallCrate
# from platform import Platform
# from spike import Spike
# from door import Door

# # COLORS
# WHITE = (255, 255, 255)
# BACKGROUND = BACKGROUND.convert_alpha()

# # SCROLLING
# MOVEMENT_BORDER_LEFT = 300
# MOVEMENT_BORDER_RIGHT = 700
# offset = 0

# # LEVELS
# LEVEL1 = "level1.json"
# LEVEL2 = "level2.json"
# LEVEL3 = "level3.json"
# # LEVELS = [LEVEL3]
# LEVELS = [LEVEL1, LEVEL2, LEVEL3]  # List of all available levels

# current_level = 0

# # FONTS
# FONT_30 = pygame.font.SysFont('comicsans', 30)
# FONT_90 = pygame.font.SysFont('comicsans', 90)

# def blit_text_center(text, win, color):
#     render = FONT_90.render(text, 1, color)
#     win.blit(render, (WIDTH // 2 - render.get_width() // 2, HEIGHT // 2 - render.get_height() // 2))

# def blit_text(text, win, font_size, color, x, y):
#     FONT = pygame.font.SysFont('comicsans', font_size)
#     render = FONT.render(text, 1, color)
#     win.blit(render, (x, y))

# def draw(win, player, objects, offset):
#     win.blit(BACKGROUND, (0, 0))
#     for block in objects:
#         block.draw(win, offset)

#     player.draw(win, offset)

#     pygame.display.update()


# def check_vertical_collision(player, objects):
#     for block in objects:
#         if abs(player.y - block.y) > 100 or abs(player.x - block.x) > 100:
#             continue

#         result = player.collide(block)
#         if not result:
#             continue

#         if result[1] < block.img.get_height():
#             player.fall()
#             break
#         elif result[1] >= block.img.get_height() / 2 and not player.jumping:
#             player.land(block)
#             break
#     else:
#         if not player.jumping:
#             player.fall()


# def check_horizontal_collision(player, objects):
#     for block in walls:
#         if abs(player.y - block.y) > 100 or abs(player.x - block.x) > 100:
#             continue

#         result = player.collide(block)
#         if not result:
#             continue

#         if result[0] >= block.img.get_width() * 2 - 10:
#             player.bounce("right", block)
#             break
#         elif result[0] < player.img[1].get_width():
#             player.bounce("left", block)
#             break
#     else:
#         player.blocked_direction = None


# def check_crate_collision(player, objects, walls):
#     for crate in objects:
#         if abs(player.y - crate.y) > 100 or abs(player.x - crate.x) > 100 or not crate.visible:
#             continue

#         result = player.collide(crate)
#         if not result:
#             continue
        
#         if crate.small and player.action_type == "attack":
#             crate.visible = False

#         if result[0] > crate.img.get_width() / 2:
#             if player.action == "push":  # right
#                 crate.x += player.vel

#                 for wall in walls:
#                     if crate.collide(wall):
#                         crate.x -= player.vel
#                         player.bounce("right", crate)
#                         break
#             else:
#                 player.bounce("right", crate)
#             break
#         elif result[0] < crate.img.get_width() / 2:
#             if player.action == "push":  # left
#                 crate.x -= player.vel

#                 for wall in walls:
#                     if crate.collide(wall):
#                         crate.x += player.vel
#                         player.bounce("left", crate)
#                         break
#             else:
#                 player.bounce("left", crate)
#             break


# def check_platform_collision(player, objects):
#     for block in objects:
#         if abs(player.y - block.y) > 100 or abs(player.x - block.x) > 100:
#             continue

#         result = player.collide(block)
#         if not result:
#             continue

#         # check vertical collision
#         if result[1] >= 32 and result[1] <= 50:
#             player.fall()
#             break
#         elif result[1] >= 80 and not player.jumping:
#             player.land(block)
#             player.x += block.x_vel
#             break

# def load_level(name):
#     floors = []
#     walls = []
#     crates = []
#     platforms = []
#     spikes = []
#     doors = []

#     with open(name, "r") as json_file:
#         level = json.load(json_file)["data"]

#     for obj in level:
#         x, y = round(obj['x']), round(obj['y'])
#         create = obj["type"]
#         if create == "floor":
#             obj = Block(x, y, BLOCKS[0])
#             floors.append(obj)
#         elif create == "wall":
#             obj = Block(x, y, BLOCKS[5])
#             walls.append(obj)
#         elif create == "crate":
#             obj = Crate(x, y)
#             crates.append(obj)
#         elif create == "platform":
#             obj = Platform(x, y)
#             platforms.append(obj)
#         elif create == "spike":
#             obj = Spike(x, y)
#             spikes.append(obj)
#         elif create == "door":
#             obj = Door(x, y)
#             doors.append(obj)

#     return floors, walls, crates, platforms, spikes, doors

# def show_main_menu(win, player):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
        
#         if event.type == pygame.KEYDOWN:
#             return False

#     win.blit(BACKGROUND, (0, 0))
#     blit_text_center("Press any key to begin!", win, (0, 0, 0))
#     blit_text("A - Move Left", win, 40, (0, 0, 0), *(10, 10))
#     blit_text("D - Move Right", win, 40, (0, 0, 0), *(10, 50))
#     blit_text("W - Enter Door", win, 40, (0, 0, 0), *(10, 90))
#     blit_text("SPACE - Jump", win, 40, (0, 0, 0), *(10, 130))
#     blit_text("F - Push Crate", win, 40, (0, 0, 0), *(10, 170))
#     blit_text("LEFT SHIFT - Sprint", win, 40, (0, 0, 0), *(10, 210))

#     player.action = "run"
#     player.set_image()
#     player.draw(win, 0)
#     pygame.display.update()

#     return True

# create_objects = {
#     "floor": Block,
#     "wall": Block,
#     "crate": Crate,
#     "platform": Platform,
#     "spike": Spike,
#     "door": Door
# }

# run = True

# player = Player(10, 350, "left", WIDTH, HEIGHT)
# dummy_player = Player(350, 400, "right", WIDTH, HEIGHT)
# dummy_player.big = True
# clock = pygame.time.Clock()

# floors, walls, crates, platforms, spikes, doors = load_level(LEVEL1)

# crates.append(SmallCrate(100, 600))

# objects = floors + walls + crates + platforms + spikes + doors
# main_menu = True

# while run:
#     clock.tick(MAX_FPS)

#     if main_menu:
#         main_menu = show_main_menu(WIN, dummy_player)
#         continue

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             break

#     keys = pygame.key.get_pressed()

#     player.move(keys)
#     player.handle_jump(keys)

#     check_vertical_collision(player, floors)
#     check_horizontal_collision(player, walls)
#     check_crate_collision(player, crates, walls)
#     check_platform_collision(player, platforms)

#     for spike in spikes:
#         if player.collide(spike):
#             player.die()
#             draw(WIN, player, objects, offset)
#             blit_text_center("You died... Try again!", WIN, (0, 0, 0))
#             pygame.display.update()
#             pygame.time.delay(3000)
#             player.reset()

#     for door in doors:
#         if player.collide(door):
#             if keys[pygame.K_w]:  # If the player presses 'W' to enter the door
#                 current_level += 1  # Move to the next level
#                 if current_level < len(LEVELS):  # Check if there's a next level
#                     floors, walls, crates, platforms, spikes, doors = load_level(LEVELS[current_level])
#                     objects = floors + walls + crates + platforms + spikes + doors
#                     offset = 0  # Reset the scroll offset
#                     player.reset()  # Reset player state
#                 else:  # If no more levels, show the "You beat the game!" message
#                     blit_text_center(f"You beat the game!", WIN, (0, 0, 0))
#                     pygame.display.update()
#                     pygame.time.delay(3000)
#                     main_menu = True  # Go back to the main menu
#                 break

#     if player.x <= MOVEMENT_BORDER_LEFT:
#         offset = player.x - MOVEMENT_BORDER_LEFT
#     elif player.x + player.img[1].get_width() >= MOVEMENT_BORDER_RIGHT:
#         offset = player.x + player.img[1].get_width() - MOVEMENT_BORDER_RIGHT

#     player.apply_gravity()

#     if current_level >= len(LEVELS):
#         blit_text_center(f"You beat the game!", WIN, (0, 0, 0))
#         pygame.display.update()
#         pygame.time.delay(3000)
#         main_menu = True
#     else:
#         draw(WIN, player, objects, offset)

# pygame.quit()

import pygame
import json
pygame.init()  # Initializes all imported pygame modules.
pygame.font.init()  # Initializes the font module in pygame.

# GAME INFORMATION
TITLE = "Hugo The Huge"  # Title of the game that will appear in the window.
MAX_FPS = 60  # The maximum frames per second the game will run.

# WINDOW
WIDTH, HEIGHT = 1000, 700  # The dimensions of the game window (width x height).
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates the game window.
pygame.display.set_caption(TITLE)  # Sets the title of the window to the defined TITLE.

# Import other classes from different files (images, player, block, etc.)
from images import *
from player import Player
from block import Block
from crate import Crate, SmallCrate
from platform import Platform
from spike import Spike
from door import Door

# COLORS
WHITE = (255, 255, 255)  # White color (RGB value).
BACKGROUND = BACKGROUND.convert_alpha()  # Ensures background image has transparency support.

# SCROLLING
MOVEMENT_BORDER_LEFT = 300  # Left limit for player movement before the screen starts scrolling.
MOVEMENT_BORDER_RIGHT = 700  # Right limit for player movement before the screen starts scrolling.
offset = 0  # Keeps track of how far the screen should scroll horizontally.

# LEVELS
LEVEL1 = "level1.json"  # The file for the first level.
LEVEL2 = "level2.json"  # The file for the second level.
LEVEL3 = "level3.json"  # The file for the third level.
LEVELS = [LEVEL1, LEVEL2, LEVEL3]  # List of all available levels.

current_level = 0  # Tracks which level is currently being played.

# FONTS
FONT_30 = pygame.font.SysFont('comicsans', 30)  # Font for smaller text (size 30).
FONT_90 = pygame.font.SysFont('comicsans', 90)  # Font for larger text (size 90).

# Function to render and center text on the screen.
def blit_text_center(text, win, color):
    render = FONT_90.render(text, 1, color)  # Renders the text with the given font and color.
    win.blit(render, (WIDTH // 2 - render.get_width() // 2, HEIGHT // 2 - render.get_height() // 2))  # Blits (draws) the text in the center.

# Function to render text at a specific position on the screen.
def blit_text(text, win, font_size, color, x, y):
    FONT = pygame.font.SysFont('comicsans', font_size)  # Select the font with the given size.
    render = FONT.render(text, 1, color)  # Render the text with the chosen font and color.
    win.blit(render, (x, y))  # Draw the text at the specified position (x, y).

# Function to draw the game screen, including the background, objects, and the player.
def draw(win, player, objects, offset):
    win.blit(BACKGROUND, (0, 0))  # Draw the background image at the top-left corner.
    for block in objects:  # Loop through all objects (blocks, crates, etc.).
        block.draw(win, offset)  # Draw each object with the correct offset (for scrolling).
    player.draw(win, offset)  # Draw the player on the screen with the correct offset.
    pygame.display.update()  # Update the screen to display the drawn objects.

# Function to check vertical collisions between the player and objects.
def check_vertical_collision(player, objects):
    for block in objects:
        if abs(player.y - block.y) > 100 or abs(player.x - block.x) > 100:  # Ignore objects far from the player.
            continue
        result = player.collide(block)  # Check for collision between the player and block.
        if not result:  # No collision detected.
            continue
        if result[1] < block.img.get_height():  # If the player is above the block.
            player.fall()  # The player falls.
            break
        elif result[1] >= block.img.get_height() / 2 and not player.jumping:  # If the player lands on the block.
            player.land(block)  # The player lands on the block.
            break
    else:
        if not player.jumping:
            player.fall()  # If no collision and the player is not jumping, fall.

# Function to check horizontal collisions between the player and walls.
def check_horizontal_collision(player, objects):
    for block in walls:
        if abs(player.y - block.y) > 100 or abs(player.x - block.x) > 100:  # Ignore objects far from the player.
            continue
        result = player.collide(block)  # Check for collision between the player and block.
        if not result:  # No collision detected.
            continue
        if result[0] >= block.img.get_width() * 2 - 10:  # Collision on the right side of the player.
            player.bounce("right", block)  # Make the player bounce back.
            break
        elif result[0] < player.img[1].get_width():  # Collision on the left side of the player.
            player.bounce("left", block)  # Make the player bounce back.
            break
    else:
        player.blocked_direction = None  # No collision detected.

# Function to check collisions between the player and crates.
def check_crate_collision(player, objects, walls):
    for crate in objects:
        if abs(player.y - crate.y) > 100 or abs(player.x - crate.x) > 100 or not crate.visible:  # Ignore crates that are far or not visible.
            continue
        result = player.collide(crate)  # Check for collision between the player and crate.
        if not result:  # No collision detected.
            continue
        if crate.small and player.action_type == "attack":  # If the player attacks a small crate.
            crate.visible = False  # The crate becomes invisible.
        if result[0] > crate.img.get_width() / 2:  # If the player is on the right side of the crate.
            if player.action == "push":  # If the player is pushing.
                crate.x += player.vel  # Move the crate to the right.
                for wall in walls:
                    if crate.collide(wall):  # Check if the crate collides with a wall.
                        crate.x -= player.vel  # Undo the movement.
                        player.bounce("right", crate)  # Make the player bounce back.
                        break
            else:
                player.bounce("right", crate)  # If not pushing, bounce the player away.
            break
        elif result[0] < crate.img.get_width() / 2:  # If the player is on the left side of the crate.
            if player.action == "push":  # If the player is pushing.
                crate.x -= player.vel  # Move the crate to the left.
                for wall in walls:
                    if crate.collide(wall):  # Check if the crate collides with a wall.
                        crate.x += player.vel  # Undo the movement.
                        player.bounce("left", crate)  # Make the player bounce back.
                        break
            else:
                player.bounce("left", crate)  # If not pushing, bounce the player away.
            break

# Function to check collisions between the player and platforms.
def check_platform_collision(player, objects):
    for block in objects:
        if abs(player.y - block.y) > 100 or abs(player.x - block.x) > 100:  # Ignore objects far from the player.
            continue
        result = player.collide(block)  # Check for collision between the player and block.
        if not result:  # No collision detected.
            continue
        if result[1] >= 32 and result[1] <= 50:  # If the player is falling onto the platform.
            player.fall()  # The player falls.
            break
        elif result[1] >= 80 and not player.jumping:  # If the player lands on the platform.
            player.land(block)  # The player lands on the platform.
            player.x += block.x_vel  # Adjust the player's position based on the platform's velocity.
            break

# Function to load a level from a JSON file and return all objects.
def load_level(name):
    floors = []
    walls = []
    crates = []
    platforms = []
    spikes = []
    doors = []

    with open(name, "r") as json_file:
        level = json.load(json_file)["data"]  # Parse the JSON file to get the level data.

    for obj in level:  # Loop through each object in the level data.
        x, y = round(obj['x']), round(obj['y'])  # Round the x and y coordinates to integers.
        create = obj["type"]  # Get the type of object to create.
        if create == "floor":  # Create a floor object.
            obj = Block(x, y, BLOCKS[0])
            floors.append(obj)
        elif create == "wall":  # Create a wall object.
            obj = Block(x, y, BLOCKS[5])
            walls.append(obj)
        elif create == "crate":  # Create a crate object.
            obj = Crate(x, y)
            crates.append(obj)
        elif create == "platform":  # Create a platform object.
            obj = Platform(x, y)
            platforms.append(obj)
        elif create == "spike":  # Create a spike object.
            obj = Spike(x, y)
            spikes.append(obj)
        elif create == "door":  # Create a door object.
            obj = Door(x, y)
            doors.append(obj)

    return floors, walls, crates, platforms, spikes, doors  # Return all created objects.

# Function to display the main menu.
def show_main_menu(win, player):
    for event in pygame.event.get():  # Check for events (like key presses or quitting).
        if event.type == pygame.QUIT:
            pygame.quit()  # Quit pygame and close the game.
            quit()  # Exit the game.

        if event.type == pygame.KEYDOWN:  # If a key is pressed, close the main menu.
            return False

    win.blit(BACKGROUND, (0, 0))  # Draw the background image.
    blit_text_center("Press any key to begin!", win, (0, 0, 0))  # Display the start message.
    blit_text("A - Move Left", win, 40, (0, 0, 0), *(10, 10))  # Display control instructions.
    blit_text("D - Move Right", win, 40, (0, 0, 0), *(10, 50))  # More instructions.
    blit_text("W - Enter Door", win, 40, (0, 0, 0), *(10, 90))  # More instructions.
    blit_text("SPACE - Jump", win, 40, (0, 0, 0), *(10, 130))  # More instructions.
    blit_text("F - Push Crate", win, 40, (0, 0, 0), *(10, 170))  # More instructions.
    blit_text("LEFT SHIFT - Sprint", win, 40, (0, 0, 0), *(10, 210))  # More instructions.

    player.action = "run"  # Set player action to run.
    player.set_image()  # Update the player's image based on action.
    player.draw(win, 0)  # Draw the player.
    pygame.display.update()  # Update the screen.

    return True  # Keep showing the main menu until the player presses a key.

# Dictionary to map object types to their respective classes.
create_objects = {
    "floor": Block,
    "wall": Block,
    "crate": Crate,
    "platform": Platform,
    "spike": Spike,
    "door": Door
}

# Main game loop
run = True
player = Player(10, 350, "left", WIDTH, HEIGHT)  # Initialize the player at position (10, 350).
dummy_player = Player(350, 400, "right", WIDTH, HEIGHT)  # Dummy player for the main menu.
dummy_player.big = True  # Set the dummy player to be big.
clock = pygame.time.Clock()  # Create a clock to control the frame rate.

floors, walls, crates, platforms, spikes, doors = load_level(LEVEL1)  # Load the first level.

crates.append(SmallCrate(100, 600))  # Add a small crate to the level.

objects = floors + walls + crates + platforms + spikes + doors  # Combine all objects into one list.
main_menu = True  # Flag to track whether the main menu is shown.

while run:  # Main game loop.
    clock.tick(MAX_FPS)  # Limit the frame rate to MAX_FPS (60).

    if main_menu:
        main_menu = show_main_menu(WIN, dummy_player)  # Show the main menu.
        continue

    for event in pygame.event.get():  # Process events (like quitting or key presses).
        if event.type == pygame.QUIT:
            run = False  # Exit the game if the user closes the window.
            break

    keys = pygame.key.get_pressed()  # Get the state of all keys.

    player.move(keys)  # Move the player based on key inputs.
    player.handle_jump(keys)  # Handle player jumping if applicable.

    check_vertical_collision(player, floors)  # Check for vertical collisions with floors.
    check_horizontal_collision(player, walls)  # Check for horizontal collisions with walls.
    check_crate_collision(player, crates, walls)  # Check for collisions with crates.
    check_platform_collision(player, platforms)  # Check for collisions with platforms.

    for spike in spikes:  # Check if the player collides with any spikes.
        if player.collide(spike):
            player.die()  # Player dies if they collide with a spike.
            draw(WIN, player, objects, offset)  # Redraw the screen.
            blit_text_center("You died... Try again!", WIN, (0, 0, 0))  # Show death message.
            pygame.display.update()  # Update the screen.
            pygame.time.delay(3000)  # Wait for 3 seconds before resetting the player.
            player.reset()  # Reset the player.

    for door in doors:  # Check if the player collides with any doors.
        if player.collide(door):
            if keys[pygame.K_w]:  # If the player presses 'W' to enter the door.
                current_level += 1  # Move to the next level.
                if current_level < len(LEVELS):  # If there's another level, load it.
                    floors, walls, crates, platforms, spikes, doors = load_level(LEVELS[current_level])
                    objects = floors + walls + crates + platforms + spikes + doors
                    offset = 0  # Reset the scroll offset.
                    player.reset()  # Reset the player state.
                else:  # If there are no more levels, show the victory message.
                    blit_text_center(f"You beat the game!", WIN, (0, 0, 0))
                    pygame.display.update()  # Update the screen.
                    pygame.time.delay(3000)  # Wait for 3 seconds before returning to the menu.
                    main_menu = True  # Go back to the main menu.
                break

    if player.x <= MOVEMENT_BORDER_LEFT:
        offset = player.x - MOVEMENT_BORDER_LEFT  # Scroll the screen if the player moves past the left border.
    elif player.x + player.img[1].get_width() >= MOVEMENT_BORDER_RIGHT:
        offset = player.x + player.img[1].get_width() - MOVEMENT_BORDER_RIGHT  # Scroll if the player moves past the right border.

    player.apply_gravity()  # Apply gravity to the player.

    if current_level >= len(LEVELS):  # If the player has completed all levels.
        blit_text_center(f"You beat the game!", WIN, (0, 0, 0))
        pygame.display.update()  # Display the victory message.
        pygame.time.delay(3000)  # Wait for 3 seconds.
        main_menu = True  # Go back to the main menu.
    else:
        draw(WIN, player, objects, offset)  # Draw the updated game screen.

pygame.quit()  # Quit pygame when the game loop ends.

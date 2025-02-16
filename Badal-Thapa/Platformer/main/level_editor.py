import pygame
import math
import json
from datetime import datetime

# Initialize pygame modules
pygame.init()

# GAME INFORMATION
TITLE = "Hugo The Huge"  # Title of the game
MAX_FPS = 60  # Maximum frames per second

# WINDOW SETTINGS
WIDTH, HEIGHT = 1000, 700  # Define the window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window with specified width and height
pygame.display.set_caption(TITLE)  # Set the window title

# Importing necessary game assets
from images import *  # Import all from images module
from player import Player  # Import Player class from player module
from block import Block  # Import Block class from block module
from crate import Crate  # Import Crate class from crate module
from platform import Platform  # Import Platform class from platform module
from spike import Spike  # Import Spike class from spike module
from door import Door  # Import Door class from door module

# COLORS
WHITE = (255, 255, 255)  # Define the white color in RGB format
BACKGROUND = BACKGROUND.convert_alpha()  # Set the background with alpha transparency

# SCROLLING SETTINGS
MOVEMENT_BORDER_LEFT = 250  # Left border for scrolling
MOVEMENT_BORDER_RIGHT = 750  # Right border for scrolling
offset = 0  # Initialize offset for scrolling

# Load level data from JSON file
LOAD_LEVEL = "level2.json"  # Name of the JSON file containing level data
with open(LOAD_LEVEL, "r") as json_file:
    level = json.load(json_file)["data"]  # Load and parse the JSON file

# Function to draw all objects on the screen
def draw(win, objects, offset):
    win.blit(BACKGROUND, (0, 0))  # Draw the background at position (0, 0)
    for name, block in objects:
        block.draw(win, offset)  # Draw each object with offset for scrolling
    pygame.display.update()  # Update the display

# Function to round values to the nearest 10
def round_to_10(x, base=10):
    return base * round(x/base)  # Round the value x to the nearest multiple of base

# Function to save objects to JSON file
def save_objects(objects):
    data = set()  # Initialize a set to store unique objects
    for name, obj in objects:
        data.add((name, obj.x, obj.y))  # Add object data to the set
    
    new_data = []
    for name, x, y in data:
        new_data.append({"type": name, "x": x, "y": y})  # Create a dictionary for each object
    
    name = LOAD_LEVEL  # Filename remains the same
    with open(name, "w") as f:
        json.dump({"data": new_data}, f)  # Save updated object data as JSON

# Game loop initialization
run = True  # Variable to control the game loop
player = Player(700, 410, "left", WIDTH, HEIGHT)  # Create player instance with initial position and direction
clock = pygame.time.Clock()  # Initialize clock for frame rate control

objects = []  # List to store game objects

# Dictionary mapping object types to their respective classes
create_objects = {
    "floor": Block,
    "wall": Block,
    "crate": Crate,
    "platform": Platform,
    "spike": Spike,
    "door": Door
}

# Load objects from the level file
for obj in level:
    create = obj["type"]
    if create == "floor":
        obj = create_objects[create](obj["x"], obj["y"], BLOCKS[0])  # Create floor object with specific block image
    elif create == "wall":
        obj = create_objects[create](obj["x"], obj["y"], BLOCKS[5])  # Create wall object with specific block image
    else:
        obj = create_objects[create](obj["x"], obj["y"])  # Create other objects
    
    objects.append((create, obj))  # Add object to the list

# Generate ground blocks dynamically for the level
for i in range(-200, 200):
    floor = Block(i * 38, 670, BLOCKS[0])  # Create floor blocks at intervals of 38 pixels
    objects.append(("floor", floor))

# Variable to track which object type is being placed
create = None

# Game loop
while run:
    clock.tick(MAX_FPS)  # Control frame rate to MAX_FPS

    left, middle, right = 0, 0, 0  # Initialize mouse button states

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for quit event
            run = False  # Exit the game loop
            break

        if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button click event
            left, middle, right = pygame.mouse.get_pressed()  # Get mouse button states

    keys = pygame.key.get_pressed()  # Get key states

    # Key bindings to select object type to create
    if keys[pygame.K_f]:
        create = "floor"
    if keys[pygame.K_w]:
        create = "wall"
    if keys[pygame.K_c]:
        create = "crate"
    if keys[pygame.K_p]:
        create = "platform"
    if keys[pygame.K_s]:
        create = "spike"
    if keys[pygame.K_d]:
        create = "door"
    if keys[pygame.K_m]:
        create = "move"

    # Move camera offset based on arrow key input
    if keys[pygame.K_RIGHT]:
        offset += 5
    if keys[pygame.K_LEFT]:
        offset -= 5

    # Get mouse position and adjust based on offset
    pos = pygame.mouse.get_pos()
    x, y = pos
    x += offset

    # Object movement logic
    if create == "move":
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            for name, obj in objects:
                if obj.clicked((x, y)):  # Check if object is clicked
                    obj.x = x - obj.img.get_width()/2  # Update object's x position
                    obj.y = y - obj.img.get_height()/2  # Update object's y position
    # Object creation logic
    elif left and create:
        x, y = round_to_10(x), round_to_10(y)  # Round coordinates to nearest 10
        if create == "floor":
            obj = create_objects[create](x, y, BLOCKS[0])  # Create floor object
        elif create == "wall":
            obj = create_objects[create](x, y, BLOCKS[5])  # Create wall object
        else:
            obj = create_objects[create](x, y)  # Create other objects
        
        objects.append((create, obj))  # Add object to the list
    # Object deletion logic
    elif right:
        for name, obj in objects:
            if obj.clicked((x, y)):  # Check if object is clicked
                objects.remove((name, obj))  # Remove object from the list
                break

    # Redraw the screen
    draw(WIN, objects, offset)

# Save the final state of objects before exiting
save_objects(objects)

# Quit pygame
pygame.quit()
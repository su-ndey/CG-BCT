from os import walk  # Import the walk function from the os module
import os  # Import the os module for interacting with the operating system
import pygame  # Import the pygame module for game development

pygame.init()

def load_player_sprites(path, scale=1, images=None):
    # Function to load player sprites from a specified directory
    # Parameters:
    # - path: The directory path where the sprite images are located
    # - scale: The scaling factor for the images, default is 1 (no scaling)
    # - images: A dictionary to store the loaded images, default is None

    if images == None:
        # If images dictionary is not provided, initialize it with empty lists for left and right directions
        images = {"left": [[], [], [], []], "right": [[], [], [], []]}

    cwd = os.getcwd()  # Get the current working directory
    path = os.path.join(cwd, path)  # Join the current working directory with the provided path

    for filename in os.listdir(path):
        # Iterate over all files in the specified directory
        _, direction_count, layer = filename.replace(".png", "").split("-")
        # Split the filename (without the .png extension) by '-' to get direction_count and layer
        direction = "left" if "left" in direction_count else "right"
        # Determine the direction based on the presence of "left" in direction_count
        count = int(direction_count.replace(direction, ""))
        # Extract the count by removing the direction part from direction_count and converting it to an integer
        layer = int(layer[-1])
        # Extract the layer by taking the last character of layer and converting it to an integer

        image_path = os.path.join(path, filename)  # Get the full path of the image file
        image = pygame.image.load(image_path)  # Load the image using pygame
        image = pygame.transform.scale(
            image, (image.get_width() * scale, image.get_height() * scale))
        # Scale the image based on the provided scale factor
        images[direction][layer].append(image)
        # Append the scaled image to the appropriate list in the images dictionary

    return images  # Return the dictionary containing the loaded images

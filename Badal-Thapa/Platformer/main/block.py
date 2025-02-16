import pygame  # Import the pygame module for game development
from base_object import AbstractObject  # Import AbstractObject class from the base_object module


class Block(AbstractObject):
    # Block class inherits from AbstractObject

    def __init__(self, x, y, img, rotation=0):
        # Initialize the Block object
        # Parameters:
        # - x: The x-coordinate of the block
        # - y: The y-coordinate of the block
        # - img: The image for the block
        # - rotation: The initial rotation angle of the block, default is 0

        super().__init__(x, y)  # Call the initializer of the parent class AbstractObject
        self.img = img.convert_alpha()  # Convert the image to include alpha transparency
        self.rotation = rotation  # Set the rotation angle
        self.rotate_image()  # Rotate the image based on the rotation angle

    def rotate_image(self):
        # Method to rotate the block's image
        self.img = pygame.transform.rotate(self.img, self.rotation)  # Rotate the image by the specified angle

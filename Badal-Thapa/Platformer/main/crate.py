from images import CRATE, SMALL_CRATE  # Import CRATE and SMALL_CRATE images from the images module
from base_object import AbstractObject  # Import AbstractObject class from the base_object module
import pygame  # Import the pygame module for game development


class Crate(AbstractObject):
    # Crate class inherits from AbstractObject
    IMG = CRATE  # Set the image for the crate to CRATE

    def __init__(self, x, y):
        # Initialize the Crate object
        # Parameters:
        # - x: The x-coordinate of the crate
        # - y: The y-coordinate of the crate
        super().__init__(x, y)  # Call the initializer of the parent class AbstractObject
        self.small = False  # Set the small attribute to False

    def collide(self, obj):
        # Method to check collision with another object
        # Parameters:
        # - obj: The other object to check collision with
        current_mask = pygame.mask.from_surface(self.img)  # Create a mask from the crate's image
        other_mask = pygame.mask.from_surface(obj.img)  # Create a mask from the other object's image
        offset = obj.x - self.x, obj.y - self.y  # Calculate the offset between the crate and the other object
        return current_mask.overlap(other_mask, offset)  # Check if the masks overlap at the given offset


class SmallCrate(Crate):
    # SmallCrate class inherits from Crate
    IMG = SMALL_CRATE  # Set the image for the small crate to SMALL_CRATE

    def __init__(self, x, y):
        # Initialize the SmallCrate object
        # Parameters:
        # - x: The x-coordinate of the small crate
        # - y: The y-coordinate of the small crate
        super().__init__(x, y)  # Call the initializer of the parent class Crate
        self.small = True  # Set the small attribute to True
        
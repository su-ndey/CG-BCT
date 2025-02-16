# Import the PLATFORM image from the images module
from images import PLATFORM
# Import the AbstractObject class from the base_object module
from base_object import AbstractObject

# Define a Platform class that inherits from AbstractObject
class Platform(AbstractObject):
    # Class-level attributes:
    # IMG stores the platform image
    IMG = PLATFORM
    # VEL defines the default velocity of the platform
    VEL = 2

    # Constructor method for initializing a Platform instance
    def __init__(self, x, y, horizontal_travel=150, vertical_travel=0):
        # Store the starting x and y positions
        self.start_x = self.x = x
        self.start_y = self.y = y
        # Set the horizontal and vertical velocities to the default VEL
        self.x_vel = self.VEL
        self.y_vel = self.VEL
        # Define how far the platform can travel horizontally and vertically
        self.horizontal_travel = horizontal_travel
        self.vertical_travel = vertical_travel
        # Convert the image to use alpha transparency (for better rendering)
        self.img = self.IMG.convert_alpha()

    # Method to move the platform
    def move(self):
        # Check if the platform has traveled the maximum horizontal distance
        if abs(self.start_x - (self.x + self.x_vel)) >= self.horizontal_travel:
            # Reverse the horizontal direction if the limit is reached
            self.x_vel *= -1

        # Move the platform horizontally if horizontal_travel is not zero
        if self.horizontal_travel != 0:
            self.x += self.x_vel

        # Check if the platform has traveled the maximum vertical distance
        if abs(self.start_y - (self.y + self.y_vel)) >= self.vertical_travel:
            # Reverse the vertical direction if the limit is reached
            self.y_vel *= -1

        # Move the platform vertically if vertical_travel is not zero
        if self.vertical_travel != 0:
            self.y += self.y_vel

    # Method to draw the platform on the screen
    def draw(self, win, offset):
        # Draw the platform image at the current position, adjusted by the offset
        win.blit(self.img, (self.x - offset, self.y))
        # Call the move method to update the platform's position
        self.move()
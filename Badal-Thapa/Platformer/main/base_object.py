import pygame  # Import the pygame module for game development

class AbstractObject:
    # Define the AbstractObject class

    IMG = None  # Class attribute to hold the image, initially set to None

    def __init__(self, x, y):
        # Initialize the AbstractObject
        # Parameters:
        # - x: The x-coordinate of the object
        # - y: The y-coordinate of the object

        self.x = x  # Set the x-coordinate of the object
        self.y = y  # Set the y-coordinate of the object
        self.img = self.IMG  # Set the image of the object to the class attribute IMG
        self.visible = True  # Set the visibility of the object to True

    def draw(self, win, offset):
        # Method to draw the object on the screen
        # Parameters:
        # - win: The window or surface to draw the object on
        # - offset: The offset for scrolling

        if self.visible:
            # Only draw the object if it is visible
            win.blit(self.img, (self.x - offset, self.y))
            # Draw the image on the window at the adjusted position

    def clicked(self, pos):
        # Method to check if the object was clicked
        # Parameters:
        # - pos: The position of the mouse click

        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        # Create a rectangle around the object based on its position and image dimensions

        return rect.collidepoint(pos)
        # Check if the mouse click position is within the rectangle

from images import *  # Import all from images module
import pygame  # Import the pygame module for game development

# Define actions and their corresponding images for different states
ACTIONS = {
    "normal": {
        "walk": PLAYER_WALK,  # Walking animation
        "run": PLAYER_RUN,  # Running animation
        "jump": PLAYER_JUMP,  # Jumping animation
        "push": PLAYER_PUSH,  # Pushing animation
        "stand": PLAYER_STAND,  # Standing animation
        "falling": PLAYER_FALLING  # Falling animation
    },
    "weapon": {
        "walk": PLAYER_WALK_WEAPON,  # Walking animation with weapon
        "run": PLAYER_RUN_WEAPON,  # Running animation with weapon
        "jump": PLAYER_JUMP_WEAPON,  # Jumping animation with weapon
        "push": PLAYER_PUSH_WEAPON,  # Pushing animation with weapon
        "stand": PLAYER_STAND_WEAPON,  # Standing animation with weapon
        "falling": PLAYER_FALLING_WEAPON  # Falling animation with weapon
    },
    "attack": {
        "chop": PLAYER_ATTACK_CHOP  # Chopping attack animation
    },
    "dead": [DEAD, DEAD, DEAD]  # Dead state animation
}

# Convert images to include alpha transparency
for key in ACTIONS:
    if key == "dead":
        continue  # Skip the dead state

    for other_key in ACTIONS[key]:
        for lr in ACTIONS[key][other_key]:
            for i, layer in enumerate(ACTIONS[key][other_key][lr]):
                new_layer = []
                for item in layer:
                    img = item.convert_alpha()  # Convert image to include alpha transparency
                    new_layer.append(img)
                ACTIONS[key][other_key][lr][i] = new_layer


class Player:
    ACTIONS = ACTIONS  # Set the actions attribute to the ACTIONS dictionary

    WALK_VEL = 3  # Walking velocity
    RUN_VEL = 5  # Running velocity
    GRAVITY = 6  # Gravity value
    JUMP_VEL = 15  # Jumping velocity
    BIG_FACTOR = 2  # Scaling factor for being "big"

    def __init__(self, x, y, direction, window_width=0, window_height=0):
        # Initialize the Player object
        # Parameters:
        # - x: The x-coordinate of the player
        # - y: The y-coordinate of the player
        # - direction: The initial direction of the player
        # - window_width: The width of the window, default is 0
        # - window_height: The height of the window, default is 0

        self.x = self.start_x = x  # Set the x-coordinate and starting x-coordinate
        self.y = self.start_y = y  # Set the y-coordinate and starting y-coordinate
        self.window_width = window_width  # Set the window width
        self.window_height = window_height  # Set the window height

        self.direction = self.starting_direction = direction  # Set the direction and starting direction
        self.action = "run"  # Set the initial action to "run"
        self.action_type = "weapon"  # Set the initial action type to "weapon"

        self.animation_count = 0  # Initialize the animation count
        self.frame_duration = 5  # Set the frame duration for animations
        self.img = None  # Initialize the image attribute
        self.vel = self.WALK_VEL  # Set the velocity to walking velocity

        self.jumping = False  # Initialize jumping state
        self.jump_count = 0  # Initialize jump count
        self.jump_duration = 20  # Set the jump duration

        self.grounded = False  # Initialize grounded state
        self.blocked_direction = None  # Initialize blocked direction

        self.big = False  # Initialize big state
        self.set_image()  # Set the initial image

    def land(self, obj):
        # Method to handle landing on an object
        self.jumping = False  # Set jumping state to False
        self.jump_count = 0  # Reset jump count
        if self.action == "falling":
            self.action = "stand"  # Change action to "stand" if falling
        while (result := self.collide(obj)):
            if result[1] < obj.img.get_height() / 2:
                break  # Break if collision is not too deep
            self.y -= 1  # Adjust y-coordinate to prevent sinking
        self.y += 1  # Adjust y-coordinate slightly
        self.grounded = True  # Set grounded state to True

    def die(self):
        # Method to handle player death
        self.action = "dead"  # Change action to "dead"
        self.set_image()  # Set the image to the dead state

    def reset(self):
        # Method to reset the player's state
        self.x = self.start_x  # Reset x-coordinate
        self.y = self.start_y  # Reset y-coordinate
        self.jumping = False  # Reset jumping state
        self.jump_count = 0  # Reset jump count
        self.jump_duration = 20  # Reset jump duration
        self.vel = self.WALK_VEL  # Reset velocity to walking velocity

        self.grounded = False  # Reset grounded state
        self.blocked_direction = None  # Reset blocked direction

        self.direction = self.starting_direction  # Reset direction
        self.action = "run"  # Reset action to "run"
        self.action_type = "weapon"  # Reset action type to "weapon"

        self.big = False  # Reset big state

    def toggle_big(self):
        # Method to toggle the big state
        self.big = not self.big  # Toggle the big state

    def fall(self):
        # Method to handle falling
        self.jumping = False  # Set jumping state to False
        self.jump_count = 0  # Reset jump count
        if not self.action_type == "attack":
            self.action = "falling"  # Change action to "falling" if not attacking
        self.grounded = False  # Set grounded state to False

    def apply_gravity(self):
        # Method to apply gravity to the player
        if not self.grounded:
            self.y += self.GRAVITY  # Apply gravity if not grounded
        elif self.jump_count == 0 and self.action == "falling":
            self.action = "stand"  # Change action to "stand" if falling and not jumping

    def set_image(self):
        # Method to set the player's image based on the current state
        if self.action == "dead":
            self.img = self.ACTIONS["dead"]  # Set image to dead state
        else:
            action = self.ACTIONS[self.action_type][self.action][self.direction]
            # Get the current action image based on action type, action, and direction
            flip = False  # Initialize flip state
            if self.action == "push" and self.direction == "right":
                flip = True  # Set flip state to True if pushing and facing right
                action = self.ACTIONS[self.action_type][self.action]["left"]
                # Get the left-facing action image for pushing

            if self.animation_count // self.frame_duration >= len(action[1]):
                self.animation_count = 0  # Reset animation count

                if self.jumping:
                    self.action = "falling"  # Change action to "falling" if jumping

                if self.action_type == "attack":
                    self.action_type = "weapon"  # Change action type to "weapon" if attacking
                    self.action = "stand"  # Change action to "stand"

            self.img = [layer[self.animation_count//self.frame_duration]
                        for layer in action if layer]
            # Set the image to the current frame of the action animation

            if flip:
                new_img = []
                for image in self.img:
                    image = pygame.transform.flip(image, True, False)
                    # Flip the image horizontally
                    new_img.append(image)
                self.img = new_img  # Set the image to the flipped version

        if self.big:
            new_img = []
            for image in self.img:
                image = pygame.transform.scale(image, (round(image.get_width(
                ) * self.BIG_FACTOR), round(image.get_height() * self.BIG_FACTOR)))
                # Scale the image based on the BIG_FACTOR
                new_img.append(image)
            self.img = new_img  # Set the image to the scaled version

    def draw(self, win, offset):
        # Method to draw the player on the screen
        for layer in self.img:
            win.blit(layer, (self.x - offset, self.y))
            # Draw each layer of the image at the adjusted position

        self.animation_count += 1  # Increment the animation count
        self.set_image()  # Update the image based on the current state

    def bounce(self, direction, obj):
        # Method to handle bouncing off an object
        self.blocked_direction = direction  # Set the blocked direction

    def move(self, keys):
        # Method to handle player movement based on key inputs
        if self.action == "dead":
            return  # Do not move if the player is dead

        prev_action, prev_direction = self.action, self.direction
        # Store the previous action and direction

        self.handle_attack()  # Handle attack inputs

        if keys[pygame.K_a] and self.blocked_direction != "left":  # Move left
            if self.action not in ["push",  "jump", "falling"] and self.action_type != "attack":
                self.action = "walk"  # Change action to "walk" if not pushing, jumping, or falling
            self.direction = "left"  # Set direction to left
            self.x -= self.vel  # Move left by the current velocity
        elif keys[pygame.K_d] and self.blocked_direction != "right":  # Move right
            if self.action not in ["push", "jump",  "falling"] and self.action_type != "attack":
                self.action = "walk"  # Change action to "walk" if not pushing, jumping, or falling
            self.direction = "right"  # Set direction to right
            self.x += self.vel  # Move right by the current velocity
        elif self.action_type != "attack" and not self.action in ["jump", "falling"]:
            self.action = "stand"  # Change action to "stand" if not attacking, jumping, or falling

        if keys[pygame.K_LSHIFT] and self.action in ["walk", "run"]:  # Run
            self.action = "run"  # Change action to "run"
            self.vel = self.RUN_VEL  # Set velocity to running velocity

        if self.jumping:
            return  # Do not perform other actions if jumping

        if keys[pygame.K_f] and self.action_type != "attack":
            self.action = "push"  # Change action to "push"

        if self.action != prev_action or self.direction != prev_direction:
            self.animation_count = 0  # Reset animation count if action or direction changed

    def handle_jump(self, keys):
        # Method to handle jumping based on key inputs
        if self.jumping:
            self.jump_count += 1  # Increment jump count
            self.y -= self.JUMP_VEL  # Move up by the jump velocity
            if self.jump_count >= self.jump_duration:
                self.jumping = False  # Stop jumping if jump duration is reached
                self.jump_count = 0  # Reset jump count
        elif keys[pygame.K_SPACE] and self.grounded and self.action_type != "attack":
            self.action = "jump"  # Change action to "jump"
            self.jumping = True  # Set jumping state to True
            self.jump_count = 1  # Initialize jump count
            self.grounded = False  # Set grounded state to False

    def handle_attack(self):
        # Method to handle attacking based on mouse inputs
        pressed = pygame.mouse.get_pressed()  # Get mouse button states

        if any(pressed) and not self.action_type == "attack":
            self.action_type = "attack"  # Change action type to "attack"
            self.action = "chop"  # Change action to "chop"

    def collide(self, obj):
        # Method to check collision with another object
        current_mask = pygame.mask.from_surface(self.img[1])  # Create a mask from the player's image
        other_mask = pygame.mask.from_surface(obj.img)  # Create a mask from the other object's image
        offset = obj.x - self.x, obj.y - self.y  # Calculate the offset between the player and the other object
        return current_mask.overlap(other_mask, offset)  # Check if the masks overlap at the given offset

import pygame


class Ship():
    """A class to represent a player ship object"""

    def __init__(self, game_settings, screen):
        """Initialize the ship and set it's starting position"""
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')

        # Load sound effect for firing the laser
#        self.laser_sound = pygame.mixer.Sound('audio/laser.wav')

        # Resize image
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ship at the bottom center of the screen
        # Match the ships center x-coordinate with the screens' centerx
        self.rect.centerx = self.screen_rect.centerx
        # Match the ships bottom y-coordinate match the screens bottomy
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on movement flags"""
        # Update ship's center value
        # Stop the ship from moving past the right side of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor

        # Stop the ship from moving past the left side of the screen
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)
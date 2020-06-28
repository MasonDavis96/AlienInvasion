import pygame

class Ship():
    """A class to represent a player ship object"""

    def __init__(self, screen):
        """Initialize the ship and set it's starting position"""
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        # Resize image
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ship at the bottom center of the screen
        # Match the ships center x-coordinate with the screens' centerx
        self.rect.centerx = self.screen_rect.centerx
        # Match the ships bottom y-coordinate match the screens bottomy
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent an alien ship object"""

    def __init__(self, game_settings, screen):
        """Initialize the alien and set it's starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # Start each alien at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at it's current location"""
        self.screen.blit(self.image, self.rect)
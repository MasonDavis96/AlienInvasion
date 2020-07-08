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


    def update(self):
        """Move the alien right"""
        self.x += (self.game_settings.alien_speed_factor *
                   self.game_settings.fleet_direction)
        self.rect.x = self.x


    def blitme(self):
        """Draw the alien at it's current location"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
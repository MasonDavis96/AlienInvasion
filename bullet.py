import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to represent/manage bullets fired from the ship"""

    def __init__(self, game_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__() # Bullet inherits from Sprite
        self.screen = screen

        # Create a bullet object at (0, 0) and then set correct position.
        # Build rectangle from scratch using pygame.Rect()
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top # Bullet comes from top of ship

        # Store the bullets position as a float
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor


    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

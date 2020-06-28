import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # The main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw screen
        screen.fill(game_settings.screen_color)
        ship.blitme()

        # Draw the most recent screen
        pygame.display.flip()


run_game()
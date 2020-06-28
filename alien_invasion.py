import pygame

from settings import Settings
from ship import Ship
import game_functions


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
        # Check key presses/mouse events
        game_functions.check_events(ship)

        # Update ship position
        ship.update()

        # Update/re-draw screen
        game_functions.update_screen(game_settings, screen, ship)


run_game()
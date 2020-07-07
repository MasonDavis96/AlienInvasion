import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(game_settings, screen)

    # Make a group to store bullets
    bullets = Group()

    # The main loop for the game
    while True:
        # Check key presses/mouse events
        game_functions.check_events(game_settings, screen, ship, bullets)

        # Update ship position
        ship.update()

        # Update bullet position (delete bullet if applicable)
        game_functions.update_bullet(bullets)

        # Update/re-draw screen
        game_functions.update_screen(game_settings, screen, ship, bullets)


run_game()
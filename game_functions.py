import sys
import pygame


def check_events(ship):
    """Check for and respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # If right arrow key is pressed
            if event.key == pygame.K_RIGHT:
                # Move ship right
                ship.moving_right = True
                # If left arrow key is pressed
            if event.key == pygame.K_LEFT:
                # Move ship left
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            # If right arrow key is released
            if event.key == pygame.K_RIGHT:
                # Stop moving right
                ship.moving_right = False
            # If left arrow key is released
            if event.key == pygame.K_LEFT:
                # Stop moving left
                ship.moving_left = False


def update_screen(game_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Redraw screen
    screen.fill(game_settings.screen_color)
    ship.blitme()

    # Draw the most recent screen
    pygame.display.flip()
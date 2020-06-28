import sys
import pygame

def check_events():
    """Check for and respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Redraw screen
    screen.fill(game_settings.screen_color)
    ship.blitme()

    # Draw the most recent screen
    pygame.display.flip()
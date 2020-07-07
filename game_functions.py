import sys
import pygame

from bullet import  Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Respond to key presses"""
    # If right arrow key is pressed
    if event.key == pygame.K_RIGHT:
        # Move ship right
        ship.moving_right = True
        # If left arrow key is pressed
    elif event.key == pygame.K_LEFT:
        # Move ship left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    # If right arrow key is released
    if event.key == pygame.K_RIGHT:
        # Stop moving right
        ship.moving_right = False
    # If left arrow key is released
    if event.key == pygame.K_LEFT:
        # Stop moving left
        ship.moving_left = False


def check_events(game_settings, screen, ship, bullets):
    """Check for and respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw screen
    screen.fill(game_settings.screen_color)

    # Draw ship
    ship.blitme()

    # Redraw all bullets behind the ship/aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the most recent screen
    pygame.display.flip()


def update_bullet(bullets):
    """Update position of the bullets. If they leave the screen,
    also deletes them"""
    # Update bullet position
    bullets.update()

    # Delete bullets that have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet from the ship if the limit has not been reached"""
    if len(bullets) < game_settings.num_bullets_allowed:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

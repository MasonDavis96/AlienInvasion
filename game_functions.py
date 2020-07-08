import sys
import pygame

from bullet import  Bullet
from alien import Alien


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(game_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw screen
    screen.fill(game_settings.screen_color)

    # Draw ship
    ship.blitme()

    # Draw aliens within group to location based on rect attribute
    aliens.draw(screen)

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

        # Play laser sound effect
#        pygame.mixer.Sound.play(ship.laser_sound)


def get_number_aliens_x(game_settings, alien_width):
    """Determine how many aliens can fit in a single row"""
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, ship_height, alien_height):
    """Determine how many rows can fit on the screen"""
    # Subtract alien height from top, ship height from bottom, and 2 alien
    # heights from bottom to leave space for player
    available_space_y = (game_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height,
                                  alien.rect.height)

    # Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create alien and place it in row
            create_alien(game_settings, screen, aliens, alien_number, row_number)
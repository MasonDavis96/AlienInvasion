class Settings():
    """A class to store all of the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (29, 41, 81)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 = right; -1 = left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.num_bullets_allowed  = 3
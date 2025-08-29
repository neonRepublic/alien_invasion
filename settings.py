class Settings:
    """Class to store settings for Alien Invasion"""

    def __init__(self):
        """Initializes game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 4.0

        #bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right and -1 for left
        self.fleet_direction = 1


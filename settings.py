class Settings:
    """Class to store settings for Alien Invasion"""



    def __init__(self):
        """Initializes game statis settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 4.0
        self.ship_limit = 3
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

        #settings for game speed
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

      

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout gameplay"""
        self.ship_speed = 2.5
        self.bullet_speed = 10.0
        self.alien_speed = 0.5
        #fleet_direction of 1 represents right, -1 left
        self.fleet_direction = 1

        #score settings
        self.alien_points = 50



    def increase_speed(self):
        """increase speed setting"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


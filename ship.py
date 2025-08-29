import pygame

class Ship:
    """Class to manage space ship"""

    def __init__(self, ai_game):
        """Initializes ship and start point."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads ship and rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        #store a float for ships exact horizontal positioning
        self.x = float(self.rect.x)

        # Flag - starts with an imobile ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ships position based on movement flags"""
        # Update ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def bliteme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """centers ship in screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
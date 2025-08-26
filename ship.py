import pygame

class Ship:
    """Class to manage space ship"""

    def __init__(self, ai_game):
        """Initializes ship and start point."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads ship and rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Flag - starts with an imobile ship
        self.moving_right = False

    def update(self):
        """Upodate ships position based on movement flags"""
        if self.moving_right:
            self.rect.x += 1

    def bliteme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manage bullets"""
    def __init__(self, ai_game):
        """creates bullet object at ships position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #creates bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet position as a float
        self.y = float(self.rect.y)
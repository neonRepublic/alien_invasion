import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class that represents a single alien"""

    def __init__(self, ai_game):
        """ initialize alien and set it to starting position""" 
        super().__init__()  
        self.screen = ai_game.screen

        # load alien image and set it rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #starts each new alien near top left

        self.rect.x = self.rect.width
        self.rect.x = self.rect.height

        #stores alien in exact horizontal position
        self.x = float(self.rect.x)    
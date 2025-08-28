import pygame
from pygame.sprite import Sprite



class Alien(Sprite):
    """class that represents a single alien"""


    def __init__(self, ai_game):
        """ initialize alien and set it to starting position""" 
        super().__init__()  
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien image and set it rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #starts each new alien near top left

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #stores alien in exact horizontal position
        self.x = float(self.rect.x)    


    def check_edges(self):
        """returns true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)


    def update(self):
        """aliens move left or right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class used to manage assets and gamne behavior"""

    def __init__(self):
        """Starts the game and creates game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        # self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #Sets background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main game loop"""
        while True:
        # Watches for key and mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraws screen on each pass through of the loop.
            self.screen.fill(self.bg_color)
            self.ship.bliteme()

            #Make most recent screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__== '__main__':
    # Make a game instane and run game
    ai = AlienInvasion()
    ai.run_game()
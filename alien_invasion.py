import sys
import pygame

class AlienInvasion:
    """Class used to manage assets and gamne behavior"""
    def __init__(self):
        """Starts the game and creates game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start main game loop"""
        while True:
        # Watches for key and mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make most recent screen visible
            pygame.display.flip()

if __name__== '__main__':
    # Make a game instane and run game
    ai = AlienInvasion()
    ai.run_game()
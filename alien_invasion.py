import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    """Class used to manage assets and gamne behavior"""


    def __init__(self):
        """Starts the game and creates game resources"""
        pygame.init()

        #starts game in inactive state
        self.game_active = False

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #creates instance to store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #Sets background color
        self.bg_color = (230, 230, 230)
        #starts game in active state
        self.game_active = True


    def _create_fleet(self):
        """creates alien fleet"""
        # create alien and keep adding until no room left
        #spacing between aliens is one alien width, height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):

            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # finish row and reset x value, increment y value
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
            """create an alien and place it in a row"""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    
    def _check_fleet_edges(self):
        """responds if alien reaches the edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """drop entire fleet and change directions"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)


    def _update_bullets(self):
        self.bullets.update()
        #gets rid of old bullets to conserve memory
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """responds to alien/bullet collision"""
        #remove bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            #destroys existing bullets and creates new fleet
            self.bullets.empty()
            self._create_fleet()

    
    def _update_aliens(self):
        """updates the position of all alien enemies if sleet it at edge"""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien/ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # look for aliens hitting bottom screen
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """check if aliens reaches bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat same as if ship is hit
                self._ship_hit()
                break
    

    def _ship_hit(self):
        """responds to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #decrement ships_left
            self.stats.ships_left -=1

            #get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause game
            sleep(0.5)
        else:
            self.game_active = False


    def _check_events(self):
        """Respond to keypress and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()


    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def fire_bullets(self):
        """creates bullet and adds to bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        """Updates images on screen then flips to new screen"""
        # Redraws screen on each pass through of the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #Make most recent screen visible
        pygame.display.flip()
            


if __name__== '__main__':
    # Make a game instane and run game
    ai = AlienInvasion()
    ai.run_game()  
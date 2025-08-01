'''
This module has a class called AlienFleet
 which is responsible for creating and handling
  the behavior of the fleet.
'''
import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    '''
    - Creates alien fleet
- Calculates the exact size of the fleet and subtracts
one or two aliens from the exact length so that the aliens
can move. We do the same for the height's top half since
we don't want any aliens in the bottom half of the screen
- Arranges the aliens into a rectangle
- Checks if the aliens have touched an edge and if the alien
has then AlienFleet is responsible for moving the fleet down
- Draw the fleet
- Check if the fleet have collided with anything
- Checks if the fleet has been destroyed
'''
    def __init__(self, game: "AlienInvasion"):
        '''
        Holds all the instance varible and
        calls the functions that need to be
         called when an object of the class is made.
        '''
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        '''
        creates the alien fleet
        '''
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h
        fleet_w, fleet_h = self.calculate_fleet_size(
            alien_w, screen_w, alien_h, screen_h
        )

        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)
        self._create_rectangle_fleet(fleet_h, fleet_w, alien_w, x_offset, alien_h, y_offset)
        
    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        '''
        Calculates how big the fleet should be
        '''
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h / 2) // alien_h

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        '''
        creates an alien and then
         adds the alien to the fleet
         '''
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def draw(self):
        '''
        draws one alien alien at a time until
         the fleet is complete
         '''
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()

    def _create_rectangle_fleet(
        self, fleet_h, fleet_w, alien_w, x_offset, alien_h, y_offset
    ):
        '''
        Arranges all the aliens so that they are in a 
        rectangle formation
        '''
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 ==0:
                    continue
                self._create_alien(current_x, current_y)

    def _check_fleet_edges(self):
        '''
        checks if the fleet has touched an edge
        '''
        alien : Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        '''
        This method moves the fleet down and is called when
        the fleet touches an edge
        '''
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def  update_fleet(self):
        '''
        updates the fleet and checks if the fleet has
        touched an edge
        '''
        self._check_fleet_edges()
        self.fleet.update()

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        '''
        calculates how much area of the screen is not taken by
        the alien fleet
        '''
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_verticle_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_verticle_space) // 2)
        return x_offset, y_offset

    def check_collisions(self, other_group):
        '''
        checks if the fleet has collided with anything
        '''
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        '''
        checks if the fleet touches the bottom of the screen
        '''
        alien: Alien
    
        for alien in self.fleet:
            if (alien.rect.bottom) >= self.settings.screen_h:
                return True
            return False

    def check_destroyed_status(self):
        '''
        checks if the fleet has been destroyed
        '''
        return not self.fleet

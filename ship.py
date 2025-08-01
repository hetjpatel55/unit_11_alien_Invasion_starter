'''
this module is responsible for making the ship
'''
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    '''
    This class shapes the ship by adding movement and giving
    the ship the ability to fire bullets
    '''
    def __init__(self, game: "Alien_invasion", arsenal: "Arsenal"):
        '''
        stores instance varibles
        and calles a method that
        centers the ship
        '''
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def update(self):
        '''
        updates where the ship
        has moved and updates
        the arsenal
        '''
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        '''
        updates where the ship has moved
        '''
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        '''
        draws the ship
        '''
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        '''
        gives the player the ability to fire a bullet
        '''
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        '''
        checks if any collisions have occured
        '''
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False

    def _center_ship(self):
        '''
        centers ship
        '''
        self.rect.midbottom = self.boundries.midbottom
        self.x = float(self.rect.x)

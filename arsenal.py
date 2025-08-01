
'''
This module is responsible for making the ship's arsenal.
'''
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    '''
    This class makes the laser and draws the laser.
    '''
    def __init__(self, game: "AlienInvasion"):
        '''
        stores instance varibles
        '''
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        '''
        updates the amount of lasers fired and removes lasers
        that have gone offscreen.
        '''
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        '''
        deletes buttets offscreen
        '''
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        '''
        draws the bullet
        '''
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        '''
        allows the player to shoot bullets if the amount of 
        bullets already fired and not destroyed is less then
        five
        '''
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False

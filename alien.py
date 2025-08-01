'''
This module makes one alien and holds all the data for the
alien
'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    '''
    This class is responsible for drawing the alien, updating
    the alien and checking if the alien has touched an edge
    '''
    def __init__(self, fleet: "AlienFleet", x: float, y: float):
        '''
        stores instance varibles and stores some images
        '''
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundries  = fleet.game.screen.get_rect()
        self.settings = fleet.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''
        sets some varibles that will be updated in the future
        when the player does something.
        '''
        temp_speed = self.settings.fleet_speed
            
            
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        '''
        Checks if the fleet has touched an edge
        '''
        return(self.rect.right >= self.boundries.right or self.rect.left <= self.boundries.left)

    def draw_alien(self):
        '''
        draws the alien
        '''
        self.screen.blit(self.image, self.rect)

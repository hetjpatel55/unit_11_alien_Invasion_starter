import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    def __init__(self, fleet: "AlienFleet", x: float, y: float):
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
        temp_speed = self.settings.fleet_speed
        #if self.check_edges():
            #self.settings.fleet_direction *= -1
            #self.y += self.settings.fleet_drop_speed
            
            
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        return(self.rect.right >= self.boundries.right or self.rect.left <= self.boundries.left)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

'''
This module is the main file, all the other modules/classes
have been imported to this file. This module gathers smaller
classes and combines them to make a game.
'''
"""
Name of Program: Alien Invasion
Author: Het Patel
Purpose: Lab 13 homework
Date: 8/1/2025
"""
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:
    '''
    This is the main class. Every other class has been
    imported into this class. This class constructs the game:
    - First of all, this class has a method that runs the game.
    - This class also plays sounds
    - checks for collisions
    - checks how many lifes the player has
    - resets game and resets level
    - displays the scores and lifes left
    displays the play button
    - checks what keys are being pressed
    - updates screen
    '''
    def __init__(self):
        '''
        Holds all the instance varibles and calls some methods
        when an object of the class is made
        '''
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)
        self.bg_file = pygame.image.load(self.settings.bg_file)
        self.bg_file = pygame.transform.scale(
            self.bg_file, (self.settings.screen_w, self.settings.screen_h)
        )
        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.8)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.8)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, "Play")
        self.game_active = False

    def run_game(self):
        '''
        runs the game as long as the player has lifes remaining
        '''
        # Game Loop
        while self.running:
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()

            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_collisions(self):
        '''
        checks for collisions, if the alien hits the ship
        or if the laser hits the alien. And if one or both
        of them are true, then the method plays a sound
        and destroys either the alien or the ship.
        '''
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_score()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()

    def _check_game_status(self):
        '''
        checks if the player has any lifes left
        and if the player is out of lifes, then
        end the game. If the player loses a life, then 
        this method is also responsible for resetting the fleet
        '''
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        '''
        resets level
        '''
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        '''
        resets game
        '''
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_score ()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _check_events(self):
        '''
        checks if the player has clicked
        or pressed a key or button
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_keyup_events(self, event):
        '''
        checks if the player has released a key or a button
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        """
        checks if the player has held down a key or a button
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()

    def _update_screen(self):
        '''
        updates screen
        '''
        self.screen.blit(self.bg_file, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_button_clicked(self):
        '''
        checks if the play button has been pressed
        '''
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


if __name__ == "__main__":
    """Test comment"""
    ai = AlienInvasion()
    ai.run_game()

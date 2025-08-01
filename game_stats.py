'''
This module is responsible
 for the gamestats such
as the score and lives
'''
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class GameStats:
    '''
    This class keeps track of all scores and lives. 
    '''
    def __init__(self, game: "AlienInvasion"):
        '''
        stores all instance varible
        and when an object of the GameStats
        class is made, then init_saved_score and
        reset_stats is called.
        '''
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_score()
        self.reset_stats()

    def init_saved_score(self):
        '''
        This method gets the high score from a file if that is
        possible
        '''
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() >  20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)

        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """
        This method saves the high score if the high score
        has been beaten
        """
        scores = {
            'hi_score': self.hi_score
        }

        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File not fount {e}')

    def reset_stats(self):
        '''
        resets the amount of lives, score, and level
        '''
        self.ships_left = self.settings.starting_ship_amount
        self.score = 0
        self.level = 1

    def update(self, collisions):
        '''
        updates all scores
        '''
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        '''
        updates max score
        '''
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        '''
        updates high score
        '''
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        '''
        updates score
        '''
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        '''
        updates level
        '''
        self.level += 1

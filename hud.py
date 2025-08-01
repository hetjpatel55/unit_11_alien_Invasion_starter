'''
This module is responsible for displaying
all the game stats
'''
import pygame.font

class HUD:
    '''
    This class is responsible for displaying
     the level, the scores, and the amount
    of lives the player has left
    '''
    def __init__(self, game):
        '''
        This method stores instance varibles and calls
        a few methods when an object of this class is made
        '''
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = game.screen.get_rect()
        self. game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20
        self.update_score()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        '''
        this method gives a path to the life image, setting up
        the image to be drawn
        '''
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.life_rect = self.life_image.get_rect()

    def _draw_lives(self):
        '''
        draws the image times the amount
        of lives the player has left
        '''
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def update_score(self):
        '''
        updates all the scores
        '''
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self):
        '''
        updates score
        '''
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundries.right - self.padding
        self.score_rect.top = self.score_rect.bottom + self.padding

    def _update_max_score(self):
        """
        updates max score
        """
        max_score_str = f'Max score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """
        updates high score
        """
        hi_score_str = f"High score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundries.centerx, self.padding)

    def update_level(self):
        """
        updates level
        """
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(
            level_str, True, self.settings.text_color, None
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def draw(self):
        '''
        draws all the scores and levels
        '''
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()

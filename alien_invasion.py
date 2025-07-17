import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)
        self.bg_file = pygame.image.load(self.settings.bg_file)
        self.bg_file = pygame.transform.scale(
            self.bg_file, (self.settings.screen_w, self.settings.screen_h)
        )
        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

    def run_game(self):
        # Game Loop
        while self.running:
            self._check_events(self)

            self._update_screen(self)
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def _update_screen(self):
        self.screen.blit(self.bg_file, (0, 0))
        self.ship.draw()
        pygame.display.flip()


if __name__ == "__main__":
    """Test comment"""
    ai = AlienInvasion()
    ai.run_game()

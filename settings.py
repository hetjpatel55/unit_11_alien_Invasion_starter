from pathlib import Path


class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.fps = 60

        self.bg_file = (
            Path.cwd()
            / "unit_11_alien_invasion_starter"
            / "Assets"
            / "images"
            / "Starbasesnow.png"
        )

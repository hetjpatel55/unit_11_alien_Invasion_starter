from pathlib import Path


class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.fps = 60

        self.bg_file = (
            Path.cwd()
            / "Assets"
            / "images"
            / "Starbasesnow-removebg.png"
        )

        self.ship_file = (
            Path.cwd()
            / "Assets"
            / "images"
            / "ship-removebg.png"
        )
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd()  / "Assets" / "images" / "laserBlast-removebg.png"

        self.laser_sound = Path.cwd()  / "Assets" / "sound" / "laser.mp3"

        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

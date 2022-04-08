class Settings:
    """A class to manage the presentation settings of Alien Invasion Game"""

    CAPTION = 'Alien Invasion'

    def __init__(self, width=1280, height=720, bg_color=(230, 230, 230)):
        self.caption = Settings.CAPTION
        self.width = width
        self.height = height
        self.bg_color = bg_color

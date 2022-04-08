class Ship():
    BACKGROUND_IMAGE = 'presentation/images/ship.bmp'

    def __init__(self, position='midbottom'):
        self.image_path = Ship.BACKGROUND_IMAGE
        self.position = position

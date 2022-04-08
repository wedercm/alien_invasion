import sys

import pygame

from presentation.ship import Ship


class AlienInvasion():
    """Overall class to manage game assets and behavior."""

    def __init__(self, settings):
        """Initialize the game, and set settings"""
        pygame.init()
        self.settings = settings
        self.ship = Ship()

    def configure(self):
        """Configure the game presentation"""
        pygame.display.set_caption(self.settings.caption)

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.bg_color = self.settings.bg_color

    def add_ship(self):
        self.image_ship_image = pygame.image.load(self.ship.image_path)
        self.ship_image_rect = self.image_ship_image.get_rect()
        self.ship_image_rect.midbottom = self.screen.get_rect().midbottom
        self.screen.blit(pygame.image.load(self.ship.image_path), self.ship_image_rect)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.add_ship()

            pygame.display.flip()

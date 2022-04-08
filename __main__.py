from functools import partial
from alien_invasion import AlienInvasion
from presentation.settings import Settings


if __name__ == '__main__':
    settings = Settings()
    alien_invasion_game = AlienInvasion(settings)

    alien_invasion_game.configure()
    alien_invasion_game.run_game()

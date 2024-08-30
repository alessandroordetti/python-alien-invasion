import sys 

import pygame
from settings import Settings
from space_ship import SpaceShip

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
       

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = SpaceShip(self)

    def run_game(self):
        self._check_events()

    def _check_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.rect.x += 10
                    elif  event.key == pygame.K_LEFT:
                        self.ship.rect.x -= 10

            self._update_screen()
            
            """ Set the framerates to 60 """
            self.clock.tick(60) 

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
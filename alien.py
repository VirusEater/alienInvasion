import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every alien is initially in the up left corner on the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the accurate horizontal location of the alien
        self.x = float(self.rect.x)

        self.y = float(self.rect.y)

    def check_edges(self):
        """If the an alien is on the edge of the screen, then return true"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the aliens towards left/right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        # self.y += 0.1
        # self.rect.y = self.y

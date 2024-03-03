import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game):
        """Initialize the ship and set its primary position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the image of te ship and get its outer rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # For each new ship, put it in the middle bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float value in attr x of the ship
        self.x = float(self.rect.x)

        # Sign of Motion
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Adjust the position of the ship according to the motion sign"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at certain location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Let the ship be in the mid bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
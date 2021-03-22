import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class für einen einzelnen Alien"""

    def __init__(self, ai_game):
        """Alien initialisieren"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Bild von Alien laden und rect erstellen
        self.image = pygame.image.load('images/alien_green.bmp')
        self.rect = self.image.get_rect()

        # Starten am oberen Bildschirm
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """True return, wenn Alien am Rand ist"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Alien links und rechts bewegen"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
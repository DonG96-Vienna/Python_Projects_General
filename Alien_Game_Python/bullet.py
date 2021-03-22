import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class für gefeuerte Kugeln vom Schiff"""

    def __init__(self, ai_game):
        """Kugel erstellen an der gleichen Position wie Schiff"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Position als Float abspeichern
        self.y = float(self.rect.y)

    def update(self):
        """Kugel soll sich nach oben bewegen"""

        self.y -= self.settings.bullet_speed
        # Position vom rect updaten
        self.rect.y = self.y

    def draw_bullet(self):
        """Kugel darstellen am Bildschirm"""
        pygame.draw.rect(self.screen, self.color, self.rect)
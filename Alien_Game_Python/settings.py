class Settings:
    """Einstellungen gespeichert und verwaltet"""

    def __init__(self):
        """Einstellungen initialisieren und Wert geben"""
        # Bildschirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Schiffleben
        self.ship_limit = 3
        # Kugeleigenschaften
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 215, 0)
        self.bullets_allowed = 3
        # Alieneigenschaften
        self.fleet_drop_speed = 10
        # Wie stark Spiel schneller wird
        self.speedup_scale = 1.1
        # Punkte mehr wert
        self.score_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Einstellungen, die sich verändern können"""
        self.ship_speed = 1.0
        self.bullet_speed = 1.0
        self.alien_speed = 0.2
        # 1 bedeutet rechts, -1 links
        self.fleet_direction = 1
        # Punkte
        self.alien_points = 50

    def increase_speed(self):
        """Geschwindigkeit und Punkte mit Faktoren multiplizieren"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
class GameStats:
    """Spielstatistiken verfolgen"""

    def __init__(self, ai_game):
        """Statistiken initialisieren"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Spiel in pausierten Modus starten
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Statistiken initialisieren, die sich ändern könenn"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
class GameStats:
    """tracks player stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        #high score never resets
        self.high_score = 0

    def reset_stats(self):
        """initialize stats that change during gameplay"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
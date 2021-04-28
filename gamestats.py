# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:49:13 2021

@author: Korisnik
"""

class GameStats():
    """Track statistic for alien invasion"""
    
    def __init__(self, ai_settings):
        """Initialize statistic"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # High score should never be reset
        self.high_score = 0
        
        # Start Alien Invasion in an active state
        self.game_active = False
    
    def reset_stats(self):
        """Initialize statistic that can change during game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
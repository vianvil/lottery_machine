import pygame

class Coins:
    """Class to manage the coins"""
    def __init__(self, lm_game):
        """Initialize the coins, and setting positions"""
        self.screen = lm_game.screen
        self.screen_rect = lm_game.screen.get_rect()

        #load the coin image, and get its rect to position
        self.image = pygame.image.load('images/coin_copper.bmp')
        self.rect = self.image.get_rect()

        #Start each coin at center of screen
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """Draw the coin at its current location"""
        self.screen.blit(self.image, self.rect)
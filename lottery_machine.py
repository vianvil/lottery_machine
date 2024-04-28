import sys
import pygame

class LotteryMachine:
    """Main class to manage game"""
    def __init__(self):
        """Initialize the game, and make resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Lottery Machine")

    
    def run_game(self):
        """Main loop to run game"""
        
        #Start main loop
        while True:

            #Watch for quit game (X button)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            #coloring the screen
            self.screen.fill((30,144,255))
            #displaying the screen
            pygame.display.flip()
        
if __name__ == '__main__':
    #Make a game instance, and run the game
    lm = LotteryMachine()
    lm.run_game()        
       
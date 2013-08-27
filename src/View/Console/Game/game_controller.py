from Game.game import Game
from View.Console.Game.game_screen import GameScreen
from View.Console.Game.round_controller import RoundController

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class GameController(ConsoleController):
    """ Controller for a Game """
    
    def __init__(self, numberOfPlayers, names):
        """ Initialize the Game Controller """
        self.game = Game(numberOfPlayers, names)
        screen = GameScreen(self.game)
        ConsoleController.__init__(self, screen, commands={ENDL:self.nextMessage})
        
    def nextMessage(self, event):
        """ Tell the screen to print the next message """
        if self.game.over:
            self.stopRunning()
        else:
            controller = RoundController(self.game.getNewRound())
            controller.run()
            
            if self.game.over:
                self.screen.message = "Game Over!"
            else:
                self.screen.message = "Round Complete!\r\nGet Ready for the next one!"
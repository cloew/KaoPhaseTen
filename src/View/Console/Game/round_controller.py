from Game.round import Round
from View.Console.Game.player_turn_controller import PlayerTurnController
from View.Console.Game.round_screen import RoundScreen
from View.Console.Game.Player.draw_controller import DrawController

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class RoundController(ConsoleController):
    """ Represents the Round Controller """
    
    def __init__(self, round):
        """ Initialize Round Controller """
        self.round = round
        screen = RoundScreen(self.round)
        ConsoleController.__init__(self, screen, commands={ENDL:self.performATurn})
        
        self.performPlayerTurn = self.performPlayerTurn()
        self.performPlayerTurn.next()
        
    def performATurn(self, event):
        """ Perform a single Player's Turn """
        self.performPlayerTurn.next()
        
    def performPlayerTurn(self):
        """ Perfrom a player's turn """
        while True:
            for player in self.round.players:
                self.screen.currentPlayer = player
                yield
                self.runPlayerTurn(player)
                
                if self.round.over:
                    self.stopRunning()
                
    def runPlayerTurn(self, player):
        """ Run the Player's Turn """
        if player.canPlay():
            self.runController(DrawController(player, self.round.gameDeck))
            self.runController(PlayerTurnController(player, self.round.players, self.round.matchPileManager, self.round.gameDeck))
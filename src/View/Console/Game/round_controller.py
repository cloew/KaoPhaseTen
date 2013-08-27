from Game.round import Round
from View.Console.Game.player_turn_controller import PlayerTurnController
from View.Console.Game.round_screen import RoundScreen

from kao_gui.console.console_controller import ConsoleController

class RoundController(ConsoleController):
    """ Represents the Round Controller """
    
    def __init__(self, round):
        """ Initialize Round Controller """
        self.round = round
        screen = RoundScreen(self.round)
        ConsoleController.__init__(self, screen)
        
    def isRunning(self):
        """ Return if the Round is still going """
        return ConsoleController.isRunning(self) and not self.round.over
        
    def performGameCycle(self):
        """ Perform a Game Cycle Event """
        for player in self.round.players:
            cards = self.round.gameDeck.draw()
            player.addToHand(cards)
            controller = PlayerTurnController(player, self.round.matchPileManager, self.round.gameDeck)
            controller.run()
from Game.round import Round
from View.Console.Game.player_turn_controller import PlayerTurnController
from View.Console.Game.round_screen import RoundScreen

from kao_gui.console.console_controller import ConsoleController

class RoundController(ConsoleController):
    """ Represents the Round Controller """
    
    def __init__(self, players):
        """ Initialize Round Controller """
        self.round = Round(players)
        screen = RoundScreen(self.round)
        ConsoleController.__init__(self, screen)
        
    def performGameCycle(self):
        """ Perform a Game Cycle Event """
        for player in self.round.players:
            cards = self.round.gameDeck.draw()
            player.addToHand(cards)
            controller = PlayerTurnController(player, self.round.matchPileManager, self.round.gameDeck)
            controller.run()
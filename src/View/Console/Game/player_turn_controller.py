from View.Console.Game.player_turn_screen import PlayerTurnScreen

from kao_gui.console.console_controller import ConsoleController

class PlayerTurnController(ConsoleController):
    """ Controller for a single player's turn """
    
    def __init__(self, player, matchPileManager):
        """ Initialize the Player Turn Controller """
        self.player = player
        self.matchPileManager = matchPileManager
        screen = PlayerTurnScreen(self.player, self.matchPileManager)
        ConsoleController.__init__(self, screen)
    
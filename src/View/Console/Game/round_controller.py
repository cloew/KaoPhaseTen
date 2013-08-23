from Game.round import Round
from View.Console.Game.round_screen import RoundScreen

from kao_gui.console.console_controller import ConsoleController

class RoundController(ConsoleController):
    """ Represents the Round Controller """
    
    def __init__(self, players):
        """ Initialize Round Controller """
        self.round = Round(players)
        screen = RoundScreen(self.round)
        ConsoleController.__init__(self, screen)
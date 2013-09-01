from View.Console.Game.Player.skip_screen import SkipScreen

from kao_console.ascii import KAO_UP, KAO_DOWN, ENDL
from kao_gui.console.console_controller import ConsoleController

class SkipController(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self, player, players):
        """ Initialize the *** Controller """
        self.players = list(players)
        self.players.remove(player)
        self.players = [player for player in self.players if not player.skipped]
        
        screen = SkipScreen(self.players)
        ConsoleController.__init__(self, screen, commands={KAO_UP:self.previous,
                                                           KAO_DOWN:self.next,
                                                           ENDL:self.skipPlayer})
        
        if len(self.players) == 1:
            self.players[0].skipped = True
        
    def performGameCycle(self):
        """ Perform a Game Cycle Event """
        if len(self.players) < 2:
            self.stopRunning()
            
    def skipPlayer(self, event):
        """ Skip the selected Player """
        if self.screen.selected is not None:
            self.screen.selected.skipped = True
            self.stopRunning()
        
    def next(self, event):
        """ Select the next player """
        self.screen.selectNextPlayer()
        
    def previous(self, event):
        """ Select the previous player """
        self.screen.selectPreviousPlayer()
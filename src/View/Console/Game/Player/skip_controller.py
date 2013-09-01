from View.Console.Game.Player.skip_screen import SkipScreen

from kao_gui.console.console_controller import ConsoleController

class SkipController(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self, player, players):
        """ Initialize the *** Controller """
        self.players = list(players)
        self.players.remove(player)
        
        screen = SkipScreen(self.players)
        ConsoleController.__init__(self, screen)
        
        if len(self.players) == 1:
            self.players[0].skipped = True
            
    
        
    def performGameCycle(self):
        """ Perform a Game Cycle Event """
        if len(self.players) < 2:
            self.stopRunning()
from View.Console.Game.Player.hit_pile_controller import HitPileController
from View.Console.Game.Player.hit_screen import HitScreen

from kao_console.ascii import KAO_UP, KAO_DOWN, ENDL
from kao_gui.console.console_controller import ConsoleController

class HitController(ConsoleController):
    """ Controller for letting the player hit on match piles """
    
    def __init__(self, player, matchPileManager):
        """ Initialize the Hit Controller """
        self.player = player
        self.matchPileManager = matchPileManager
        screen = HitScreen(matchPileManager)
        ConsoleController.__init__(self, screen, commands={KAO_UP:self.previous,
                                                           KAO_DOWN:self.next,
                                                           ENDL:self.tryToHitAMatch})
        
    def tryToHitAMatch(self, event):
        """ Try to Hit the selected match pile """
        self.runController(HitPileController(self.player, self.screen.selected))
        
    def next(self, event):
        """ Select the next match pile """
        self.screen.selectNextPile()
        
    def previous(self, event):
        """ Select the previous match pile """
        self.screen.selectPreviousPile()
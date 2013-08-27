from View.Console.Game.Player.player_header_view import PlayerHeaderView

from kao_gui.console.console_widget import ConsoleWidget

class DrawScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, player):
        """ Initialize the view """
        self.headerView = PlayerHeaderView(player, player.matchPileManager)
        
    def draw(self):
        """ Draw the Widget """
        self.headerView.draw()
        print "1. Draw from deck.\r"
        print "2. Draw from discard pile.\r"
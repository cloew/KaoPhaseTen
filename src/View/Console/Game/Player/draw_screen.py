from View.Console.Game.Player.player_header_view import PlayerHeaderView

from kao_gui.console.console_widget import ConsoleWidget

class DrawScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, player, gameDeck):
        """ Initialize the view """
        self.gameDeck = gameDeck
        self.headerView = PlayerHeaderView(player, gameDeck, player.matchPileManager)
        
    def draw(self):
        """ Draw the Widget """
        self.headerView.draw()
        print "1. Draw from deck.\r"
        if self.gameDeck.canDrawFromDiscard():
            print "2. Draw from discard pile.\r"
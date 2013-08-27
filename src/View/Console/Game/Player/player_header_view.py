from View.Console.Game.hand_view import HandView
from View.Console.Game.match_pile_view import MatchPileView

from kao_gui.console.console_widget import ConsoleWidget

class PlayerHeaderView(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, player, matchPileManager):
        """ Initialize the view """
        self.player = player
        self.handView = HandView(player)
        self.matchPileView = MatchPileView(matchPileManager)
        
    def draw(self):
        """ Draw the Widget """
        print "{0}'s Turn\r".format(self.player)
        print "\r"
        self.matchPileView.draw()
        print "\r"
        self.handView.draw()
from hand_view import HandView
from match_pile_view import MatchPileView

class PlayerTurnScreen:
    """ Represents the screen for a player turn """
    
    def __init__(self, player, matchPileManager):
        """ Initialize the Screen """
        self.player = player
        self.handView = HandView(player)
        self.matchPileView = MatchPileView(matchPileManager)
    
    def draw(self):
        """ Draw the Round Screen """
        self.matchPileView.draw()
        print "\r"
        self.handView.draw()
        
        print "1: Try to complete the phase.\r"
        print "2: Discard and end turn."
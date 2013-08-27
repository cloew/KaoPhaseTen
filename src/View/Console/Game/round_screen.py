from hand_view import HandView
from match_pile_view import MatchPileView

class RoundScreen:
    """ Represents the screen for a round """
    
    def __init__(self, round):
        """ Initialize the Screen """
        self.round = round
        self.matchPileView = MatchPileView(self.round.matchPileManager)
        self.currentPlayer = self.round.players[0]
    
    def draw(self):
        """ Draw the Round Screen """
        self.matchPileView.draw()
        print "\r"
        
        print "{0}'s Turn.\r".format(self.currentPlayer)
        print "Press Enter when ready to begin.\r"
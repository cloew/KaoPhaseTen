from hand_view import HandView
from match_pile_view import MatchPileView

class RoundScreen:
    """ Represents the screen for a round """
    
    def __init__(self, round):
        """ Initialize the Screen """
        self.round = round
        self.handViews = []
        for player in self.round.players:
            self.handViews.append(HandView(player))
        self.matchPileView = MatchPileView(self.round.matchPileManager)
    
    def draw(self):
        """ Draw the Round Screen """
        self.matchPileView.draw()
        print "\r"
        for handView in self.handViews:
            handView.draw()
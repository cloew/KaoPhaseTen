
class MatchPileManager:
    """ Manages all the current match piles """
    
    def __init__(self):
        """ Initialize the Match Pile Manager """
        self.piles = []
        
    def addPile(self, matchPile):
        """ Add match pile in piles """
        self.piles.append(matchPile)
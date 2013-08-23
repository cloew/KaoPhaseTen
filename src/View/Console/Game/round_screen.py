
class RoundScreen:
    """ Represents the screen for a round """
    
    def __init__(self, round):
        """ Initialize the Screen """
        self.round = round
    
    def draw(self):
        """ Draw the Round Screen """
        if len(self.round.matchPileManager.piles) == 0:
            print "Match Piles\r"
            for matchPile in self.round.matchPileManager.piles:
                print "{0}\r".format(matchPile.cards)
        
        print "\r"
        print "Hand\r"
        for player in self.round.players:
            print "{0}\r".format(player.hand)
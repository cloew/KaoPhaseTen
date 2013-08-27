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
        print "\r"
        print "Discard a Card\r"
        
        characters = ['1','2','3','4','5','6','7','8','9','0','-']
        for i in range(len(self.player.hand)):
            print "{0}: {1}\r".format(characters[i], self.player.hand[i])
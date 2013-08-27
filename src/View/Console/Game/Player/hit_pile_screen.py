
class HitPileScreen:
    """ Represents the view for htting a pile with a card """
    
    def __init__(self, player, matchPile):
        """ Initialize the view """
        self.player = player
        self.matchPile = matchPile
        
    def draw(self):
        """ Draw the screen """
        print "Pile for {0}\r".format(self.matchPile.match)
        print "{0}\r".format(self.matchPile.cards)
        print "\r"
        print "Select card to hit with:\r"
        characters = ['1','2','3','4','5','6','7','8','9','0','-']
        for i in range(len(self.player.hand)):
            print "{0}: {1}\r".format(characters[i], self.player.hand[i])
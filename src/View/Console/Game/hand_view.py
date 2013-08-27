
class HandView:
    """ View for the Hand """
    
    def __init__(self, player):
        """ Initialize the Match Pile Manager """
        self.player = player
        
    def draw(self):
        """ Draw the Match Piles """
        print "Hand\r"
        print "{0}\r".format(self.player.hand)
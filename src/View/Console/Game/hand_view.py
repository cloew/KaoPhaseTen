
class HandView:
    """ View for the Hand """
    
    def __init__(self, players):
        """ Initialize the Match Pile Manager """
        self.players = players
        
    def draw(self):
        """ Draw the Match Piles """
        print "Hand\r"
        for player in self.players:
            print "{0}\r".format(player.hand)
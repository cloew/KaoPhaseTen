
class DiscardScreen:
    """ Screen for the Player to Discard a card from their hand """
    
    def __init__(self, player):
        """ Initialize the Screen """
        self.player = player
    
    def draw(self):
        """ Draw the Round Screen """
        print "Discard a Card\r"
        
        characters = ['1','2','3','4','5','6','7','8','9','0','-']
        for i in range(len(self.player.hand)):
            print "{0}: {1}\r".format(characters[i], self.player.hand[i])
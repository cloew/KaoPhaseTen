
class HitScreen:
    """ Represents the view for a *** """
    
    def __init__(self, matchPileManager):
        """ Initialize the view """
        self.matchPiles = matchPileManager.piles
        self.selected = self.matchPiles[0]
        
    def draw(self):
        """ Draw the Matches """
        for pile in self.matchPiles:
            if pile is self.selected:
                print "--> {0}\r".format(pile.cards)
            else:
                print "    {0}\r".format(pile.cards)
                
    def selectNextPile(self):
        """ Select the Next Pile, if possible """
        index = self.matchPiles.index(self.selected)
        index += 1
        if index < len(self.matchPiles):
            self.selected = self.matchPiles[index]
            
    def selectPreviousPile(self):
        """ Select the Previous Pile, if possible """
        index = self.matchPiles.index(self.selected)
        index -= 1
        if index >= 0:
            self.selected = self.matchPiles[index]
from View.Console.Game.Card.card_list_view import CardListView
from View.Console.Game.Card.card_selection_view import CardSelectionView

class HitPileScreen:
    """ Represents the view for htting a pile with a card """
    
    def __init__(self, player, matchPile):
        """ Initialize the view """
        self.player = player
        self.matchPile = matchPile
        
    def draw(self):
        """ Draw the screen """
        print "Pile for {0}\r".format(self.matchPile.match)
        print "{0}\r".format(CardListView(self.matchPile.cards).draw())
        print "\r"
        print "Select card to hit with:\r"
        
        cardSelectionView = CardSelectionView(self.player.hand)
        cardSelectionView.draw()
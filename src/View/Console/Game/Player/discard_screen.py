from View.Console.Game.Card.card_selection_view import CardSelectionView

class DiscardScreen:
    """ Screen for the Player to Discard a card from their hand """
    
    def __init__(self, player):
        """ Initialize the Screen """
        self.player = player
    
    def draw(self):
        """ Draw the Round Screen """
        print "Discard a Card\r"
        cardSelectionView = CardSelectionView(self.player.hand)
        cardSelectionView.draw()
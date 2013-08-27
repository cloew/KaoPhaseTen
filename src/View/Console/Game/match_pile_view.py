from View.Console.Game.Card.card_list_view import CardListView

class MatchPileView:
    """ View for the Match Piles """
    
    def __init__(self, matchPileManager):
        """ Initialize the Match Pile Manager """
        self.matchPileManager = matchPileManager
        
    def draw(self):
        """ Draw the Match Piles """
        if len(self.matchPileManager.piles) > 0:
            print "Match Piles\r"
            for matchPile in self.matchPileManager.piles:
                cardListView = CardListView(matchPile.cards)
                print "{0}\r".format(cardListView.draw())
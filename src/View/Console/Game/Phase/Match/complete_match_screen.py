from View.Console.Game.Card.card_list_view import CardListView
from View.Console.Game.Card.card_selection_view import CardSelectionView

class CompleteMatchScreen:
    """ Represents the view for Completing a Match """
    
    def __init__(self, match, availableCards, matchesToCards):
        """ Initialize the view """
        self.match = match
        self.availableCards = availableCards
        self.matchesToCards = matchesToCards
        
    def draw(self):
        """ Draw the Screen """
        print "{0} -- {1}\r".format(self.match, self.match.matched(self.matchesToCards[self.match]))
        print "{0}\r".format(CardListView(self.matchesToCards[self.match]).draw())
        print "\r"
        print "Add a Card to the match\r"
        
        cardSelectionView = CardSelectionView(self.availableCards)
        cardSelectionView.draw()
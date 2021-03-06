from View.Console.Game.Card.card_view_factory import GetCardView

from kao_gui.console.console_widget import ConsoleWidget

class CardListView(ConsoleWidget):
    """ Represents the view for a Card List """
    
    def __init__(self, cards):
        """ Initialize the view """
        cardViews = [GetCardView(card) for card in cards]
        self.cardStrings = [cardView.draw() for cardView in cardViews]
        
    def draw(self):
        """ Draw the Widget """
        return "{0}".format(" ".join(self.cardStrings))
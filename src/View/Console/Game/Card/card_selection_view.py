from View.Console.Game.Card.card_view_factory import GetCardView

from kao_gui.console.console_widget import ConsoleWidget

class CardSelectionView(ConsoleWidget):
    """ Represents the view for selecting a card from a list """
    
    def __init__(self, cards):
        """ Initialize the view """
        self.cards = cards
        
    def draw(self):
        """ Draw the Widget """
        characters = ['1','2','3','4','5','6','7','8','9','0','-']
        for i in range(len(self.cards)):
            print "{0}: {1}\r".format(characters[i], GetCardView(self.cards[i]).draw())
from View.Console.Game.Card.card_list_view import CardListView

class HandView:
    """ View for the Hand """
    
    def __init__(self, player):
        """ Initialize the Match Pile Manager """
        self.player = player
        
    def draw(self):
        """ Draw the Match Piles """
        cardListView = CardListView(self.player.hand)
        print "Hand\r"
        print "{0}\r".format(cardListView.draw())
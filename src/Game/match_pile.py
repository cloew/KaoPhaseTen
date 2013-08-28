
class MatchPile:
    """ Represents a Match Pile """
    
    def __init__(self, match, cards):
        """ Initialize the Match Pile """
        self.match = match
        self.cards = cards
        self.savePile()
        
    def matches(self, card):
        """ Returns if adding the card still has the pile match """
        return self.match.matched(self.cards + [card])
        
    def add(self, card):
        """ Add a card to the pile """
        self.cards.append(card)
        self.savePile()
        
    def savePile(self):
        """ Save the Pile """
        self.cards.sort()
        self.match.matched(self.cards, store=True)
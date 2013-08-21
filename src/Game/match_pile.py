
class MatchPile:
    """ Represents a Match Pile """
    
    def __init__(self, match, cards):
        """ Initialize the Match Pile """
        self.match = match
        self.cards = cards
        
    def matches(self, card):
        """ Returns if adding the card still has the pile match """
        return self.match.matches(self.cards + [card])
        
    def add(self, card):
        """ Add a card to the pile """
        self.cards.append(card)
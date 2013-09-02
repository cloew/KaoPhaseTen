from Game.Card.number_card import NumberCard

class WildCard:
    """ Represents a Wild Card """
    type = "WILD"
    canBeDrawnFromDiscard = True
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        if hasattr(self, "number") and other.type is NumberCard.type:
            return self.number.__cmp__(other.number)
        else:
            return cmp(self.type, other.type)
        
    def __repr__(self):
        """ Return the String representation """
        return "W"
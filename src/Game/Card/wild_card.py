from Game.Card.number_card import NumberCard

class WildCard:
    """ Represents a Wild Card """
    type = "WILD"
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        if self.type is NumberCard.type and other.type is NumberCard.type:
            return self.number.__cmp(other.number)
        else:
            return cmp(self.type, other.type)
                
    @property
    def type(self):
        """ Return the type of the Wild Card """
        if hasattr(self, "number"):
            return NumberCard.type
        else:
            return WildCard.type
        
    def __repr__(self):
        """ Return the String representation """
        return "W"
from Game.Card.number_card import NumberCard

class WildCard:
    """ Represents a Wild Card """
    type = "WILD"
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        if self.type is NumberCard.type and other.type is NumberCard.type:
            if self.number < other.number:
                return -1
            elif self.number > other.number:
                return 1
            else:
                return -1
        else:
            if self.type < other.type:
                return -1
            elif self.type > other.type:
                return 1
            else:
                return 0
                
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
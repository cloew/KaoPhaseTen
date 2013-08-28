
class WildCard:
    """ Represents a Wild Card """
    type = "WILD"
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        if self.type < other.type:
            return -1
        elif self.type > other.type:
            return 1
        else:
            return 0
        
    def __repr__(self):
        """ Return the String representation """
        return "W"

class NumberCard:
    """ Represents a number card """
    type = "NUMBER"
    
    def __init__(self, number, color):
        """ Initialize the Number Card """
        self.number = number
        self.color = color
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        if hasattr(other, "number"):
            retVal = self.number.__cmp__(other.number)
            if retVal == 0:
                return self.color.__cmp__(other.color)
            return retVal
        else:
            return cmp(self.type, other.type)
        
    def __repr__(self):
        """ Return the String representation """
        return str(self.number)
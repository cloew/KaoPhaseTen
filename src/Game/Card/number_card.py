
class NumberCard:
    """ Represents a number card """
    type = "NUMBER"
    
    def __init__(self, number, color):
        """ Initialize the Number Card """
        self.number = number
        self.color = color
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        if self.type < other.type:
            return -1
        elif self.type > other.type:
            return 1
        else:
            if self.number < other.number:
                return -1
            elif self.number > other.number:
                return 1
            else:
                if self.color < other.color:
                    return -1
                elif self.color > other.color:
                    return 1
                else:
                    return 0
        
    def __repr__(self):
        """ Return the String representation """
        return str(self.number)
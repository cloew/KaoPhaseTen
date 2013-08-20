
class NumberCard:
    """ Represents a number card """
    
    def __init__(self, number, color):
        """ Initialize the Number Card """
        self.number = number
        self.color = color
        
    def __repr__(self):
        """ Return the String representation """
        return str(self.number)
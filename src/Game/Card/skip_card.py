
class SkipCard:
    """ Represents the Phase Ten Skip Card """
    type = "SKIP"
    canBeDrawnFromDiscard = False
    
    def __init__(self):
        """ Initialize the Skip Card """
        self.player = None
        
    def __cmp__(self, other):
        """ Compare a card to another card """
        return cmp(self.type, other.type)
        
    def __repr__(self):
        """ Return the String representation """
        return "S"
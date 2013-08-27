
class Run:
    """ Represents a run match """
    
    def __init__(self, count):
        """ Initialize the Number Set """
        self.count = count
        
    def matched(self, cards):
        """ Returns if the set of cards matches this match """
        start = -1
        stop = -1
        
        cardNumbers = [card.number for card in cards if hasattr(card, "number")]
        cardNumbers.sort()
        for number in cardNumbers:
            if start == -1:
                start = number
                stop = number
            elif number == (start-1):
                start = number
            elif number == (stop+1):
                stop = number
            else:
                return False
        
        return stop-start+1 >= self.count
            
    def __repr__(self):
        """ Return the String Representation of the Run """
        return "Run of {0}".format(self.count)

class NumberSet:
    """ Represents a number set """
    
    def __init__(self, count):
        """ Initialize the Number Set """
        self.count = count
        
    def matched(self, cards):
        """ Returns if the set of cards matches this match """
        count = 0
        number = -1
        for card in cards:
            if hasattr(card, "number"):
                if number == -1:
                    number = card.number
                    
                if number == card.number:
                    count += 1
                else:
                    return False
        
        return count >= self.count
            
    def __repr__(self):
        """ Return the String Representation of the Numbered Set """
        return "Numbered Set of {0}".format(self.count)
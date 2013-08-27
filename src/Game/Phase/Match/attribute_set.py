
class AttributeSet:
    """ Represents a set based on a card attribute """
    
    def __init__(self, count):
        """ Initialize the Number Set """
        self.count = count
        
    def matched(self, cards):
        """ Returns if the set of cards matches this match """
        count = 0
        cardSetValue = -1
        for card in cards:
            if hasattr(card, self.comparisonAttribute):
                if cardSetValue == -1:
                    cardSetValue = getattr(card, self.comparisonAttribute)
                    
                if cardSetValue == getattr(card, self.comparisonAttribute):
                    count += 1
                else:
                    return False
        
        return count >= self.count
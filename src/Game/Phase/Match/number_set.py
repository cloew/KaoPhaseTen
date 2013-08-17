
class NumberSet:
    """ Represents a number set """
    
    def __init__(self, count):
        """ Initialize the Number Set """
        self.count = count
        
    def matched(self, cards):
        """ Returns if the set of cards matches this match """
        matchCounts = {}
        for card in cards:
            if hasattr(card, "number"):
                if card.number in matchCounts:
                    matchCounts[card.number] += 1
                else:
                    matchCounts[card.number] = 1
                    
        for number in matchCounts:
            if matchCounts[number] >= self.count:
                return True
        else:
            return False 
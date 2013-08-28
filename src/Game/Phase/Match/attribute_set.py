from Game.Card.number_card import NumberCard
from Game.Card.wild_card import WildCard

class AttributeSet:
    """ Represents a set based on a card attribute """
    
    def __init__(self, count):
        """ Initialize the Number Set """
        self.count = count
        
    def matched(self, cards, store=False):
        """ Returns if the set of cards matches this match """
        count = 0
        cardSetValue = -1
        for card in cards:
            if card.type is NumberCard.type:
                if cardSetValue == -1:
                    cardSetValue = getattr(card, self.comparisonAttribute)
                    
                if cardSetValue == getattr(card, self.comparisonAttribute):
                    count += 1
                else:
                    return False
            elif card.type is WildCard.type:
                count += 1
            else:
                return False
        
        return count >= self.count
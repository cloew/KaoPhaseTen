from Game.Card.number_card import NumberCard
from Game.Card.wild_card import WildCard

class Run:
    """ Represents a run match """
    
    def __init__(self, count):
        """ Initialize the Number Set """
        self.count = count
        
    def matched(self, cards, store=False):
        """ Returns if the set of cards matches this match """
        start = -1
        stop = -1
        
        wildCardIndices = [cards.index(card) for card in cards if card.type is WildCard.type and not hasattr(card, "number")]
        cardNumbers = [card.number for card in cards if hasattr(card, "number")]
        cardNumbers.sort()
        
        for index in wildCardIndices:
            cardNumbers[index:index] = [cardNumbers[index-1]+1]
            if store:
                cards[index].number = cardNumbers[index-1]+1
        
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
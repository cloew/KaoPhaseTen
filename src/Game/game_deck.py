from Game.globals import colors
from Game.Card.number_card import NumberCard
from Game.Card.skip_card import SkipCard
from Game.Card.wild_card import WildCard

from kao_deck.deck import Deck
from kao_deck.deck_initializer import DeckInitializer

class GameDeck(Deck):
    """ Represents the Phase Ten Game Deck """
    
    def __init__(self):
        """ Initialize the Game Deck """
        deckInitializer = self.buildDeckInitializer()
        Deck.__init__(self, deck_initializer=deckInitializer)
        self.shuffle()
        cards = self.draw()
        self.discard(cards[0])
        
    def canDrawFromDiscard(self):
        """ Return if the top card in the discard can be drawn """
        topCard = self.topOfDiscardPile()
        return topCard is not None and topCard.canBeDrawnFromDiscard 
        
    def buildDeckInitializer(self):
        """ Build the Deck Initializer """
        deckInitializer = DeckInitializer()
        
        for i in range(1, 13):
            for color in colors:
                card = NumberCard(i, color)
                deckInitializer.addSameItem(card, 2)
                
        deckInitializer.addSameItem(WildCard(), 8)
        deckInitializer.addSameItem(SkipCard(), 4)
                
        return deckInitializer
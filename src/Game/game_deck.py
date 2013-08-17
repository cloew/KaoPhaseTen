from Game.globals import colors
from Game.Card.number_card import NumberCard

from kao_deck.deck import Deck
from kao_deck.deck_initializer import DeckInitializer

class GameDeck(Deck):
    """ Represents the Phase Ten Game Deck """
    
    def __init__(self):
        """ Initialize the Game Deck """
        deckInitializer = self.buildDeckInitializer()
        Deck.__init__(deck_initializer=deckInitializer)
        
    def buildDeckInitializer(self):
        """ Build the Deck Initializer """
        deckInitializer = DeckInitializer()
        
        for i in range(1, 13):
            for color in colors:
                card = NumberCard(i, color)
                deckInitializer.addSameItem(card, 2)
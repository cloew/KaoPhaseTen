from Game.game_deck import GameDeck

class Round:
    """ Represents a round of the game Phase Ten """
    
    def __init__(self, players):
        """ Initialize the Round with the players who are playing """
        self.players = players
        self.gameDeck = GameDeck()
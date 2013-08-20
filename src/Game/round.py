from Game.game_deck import GameDeck

class Round:
    """ Represents a round of the game Phase Ten """
    
    def __init__(self, players):
        """ Initialize the Round with the players who are playing """
        self.players = players
        self.gameDeck = GameDeck()
        
        for player in self.players:
            player.addToHand(self.gameDeck.draw(10))
            
    @property
    def over(self):
        """ Returns if the Round is over """
        for player in self.players:
            if len(player.hand) == 0:
                return True
        else:
            return False 
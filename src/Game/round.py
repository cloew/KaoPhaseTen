from Game.game_deck import GameDeck
from Game.match_pile_manager import MatchPileManager

class Round:
    """ Represents a round of the game Phase Ten """
    
    def __init__(self, players):
        """ Initialize the Round with the players who are playing """
        self.players = players
        self.gameDeck = GameDeck()
        self.matchPileManager = MatchPileManager()
        
        for player in self.players:
            player.matchPileManager = MatchPileManager()
            player.addToHand(self.gameDeck.draw(10))
            
    @property
    def over(self):
        """ Returns if the Round is over """
        for player in self.players:
            if len(player.hand) == 0:
                return True
        else:
            return False 
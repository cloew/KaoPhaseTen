from Game.game_deck import GameDeck
from Game.match_pile_manager import MatchPileManager
from Game.Player.player_round_wrapper import PlayerRoundWrapper

class Round:
    """ Represents a round of the game Phase Ten """
    
    def __init__(self, players):
        """ Initialize the Round with the players who are playing """
        self.players = []
        self.gameDeck = GameDeck()
        self.matchPileManager = MatchPileManager()
        
        for player in players:
            playerWrapper = PlayerRoundWrapper(player, self.gameDeck.draw(10), self.matchPileManager)
            self.players.append(playerWrapper)
            
    @property
    def over(self):
        """ Returns if the Round is over """
        for player in self.players:
            if len(player.hand) == 0:
                return True
        else:
            return False 
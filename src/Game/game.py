from Game.round import Round
from Game.Phase.standard_phase_list import StandardPhaseList
from Game.Player.player import Player

class Game:
    """ Represents an entire game of Phase Ten """
    
    def __init__(self, numberOfPlayers,  phaseList=StandardPhaseList):
        """ Initialize the game """
        self.players = []
        for i in range(numberOfPlayers):
            self.players.append(Player(phaseList))
            
    def getNewRound(self):
        """ Returns a new round for the game """
        return Round(self.players)
            
    @property
    def over(self):
        """ Returns if the game is over """
        for player in self.players:
            if player.phase is None:
                return True
        else:
            return False 
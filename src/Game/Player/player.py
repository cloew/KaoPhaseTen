from Game.match_pile import MatchPile

class Player:
    """ Represents a Player """
    
    def __init__(self, phaseList):
        """ Initialize the Player """
        self.phaseList = phaseList
        self.phase = phaseList.startingPhase
        
    def completePhase(self):
        """ Completes the Player's current phase """
        self.phase = self.phaseList.nextPhase(self.phase)

class Player:
    """ Represents a Player """
    
    def __init__(self, name, phaseList):
        """ Initialize the Player """
        self.name = name
        self.phaseList = phaseList
        self.phase = phaseList.startingPhase
        
    def completePhase(self):
        """ Completes the Player's current phase """
        self.phase = self.phaseList.nextPhase(self.phase)
        
    def __repr__(self):
        """ Return the string representation of the Player """
        return self.name
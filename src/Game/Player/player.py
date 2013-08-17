
class Player:
    """ Represents a Player """
    
    def __init__(self, phaseList):
        """ Initialize the Player """
        self.hand = []
        self.phaseList = phaseList
        self.phase = phaseList.startPhase
    
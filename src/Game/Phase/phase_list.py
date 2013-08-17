
class PhaseList:
    """ Represents the list of Phases for a game of Phase 10 """
    
    def __init__(self, phases):
        """ Initialize the Phase List """
        self.phases = phase
        
    @property
    def startingPhase(self):
        """ Return the starting phase """
        return self.phases[0]
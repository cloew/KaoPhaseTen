
class PhaseList:
    """ Represents the list of Phases for a game of Phase 10 """
    
    def __init__(self, phases):
        """ Initialize the Phase List """
        self.phases = phases
        
    @property
    def startingPhase(self):
        """ Return the starting phase """
        return self.phases[0]
        
    def nextPhase(self, currentPhase):
        """ Returns the next Phase """
        index = self.phases.index(currentPhase)
        if index+1 < len(self.phases):
            return self.phases[index+1]
        return None 
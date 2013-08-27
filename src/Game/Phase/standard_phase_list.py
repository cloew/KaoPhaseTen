from Game.Phase.phase import Phase
from Game.Phase.phase_list import PhaseList
from Game.Phase.Match.number_set import NumberSet
from Game.Phase.Match.run import Run

class StandardPhaseList(PhaseList):
    """ Represents the standard Phase List """
    
    def __init__(self):
        """ Initialize Standard Phase List """
        PhaseList.__init__(self, self.buildPhases())
        
    def buildPhases(self):
        """ Builds and returns the standard phases in a list """
        phase = Phase([NumberSet(3), NumberSet(3)])
        phase2 = Phase([NumberSet(3), Run(4)])
        phase9 = Phase([NumberSet(5), NumberSet(2)])
        return [phase, phase2, phase9]
        
StandardPhaseList = StandardPhaseList()
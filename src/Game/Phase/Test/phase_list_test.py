from Game.Phase.phase import Phase
from Game.Phase.phase_list import PhaseList

import unittest

class nextPhase(unittest.TestCase):
    """ Test cases of nextPhase """
    
    def  setUp(self):
        """ Build the Phases and Phase List for the test """
        self.phase1 = Phase([])
        self.phase2 = Phase([])
        self.phaseList = PhaseList([self.phase1, self.phase2])
        
    def properPhase(self):
        """ Test that the proper Phase is returned when given a Phase """
        assert self.phaseList.nextPhase(self.phase1) == self.phase2, "The Second phase should be the next phase after the first phase"
        
    def noNextPhase(self):
        """ Test that None is returned when there is no next phase """
        assert self.phaseList.nextPhase(self.phase2) is None, "There is no phase after the last phase"

# Collect all test cases in this class
testcasesNextPhase = ["properPhase", "noNextPhase"]
suiteNextPhase = unittest.TestSuite(map(nextPhase, testcasesNextPhase))

##########################################################

# Collect all test cases in this file
suites = [suiteNextPhase]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
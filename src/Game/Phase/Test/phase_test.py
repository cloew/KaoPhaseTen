from Game.Card.number_card import NumberCard
from Game.Phase.phase import Phase
from Game.Phase.Match.number_set import NumberSet

import unittest

class completable(unittest.TestCase):
    """ Test cases of completable """
    
    def  setUp(self):
        """ Build the Phase for the test """
        self.match1 = NumberSet(1)
        self.match2 = NumberSet(1)
        self.phase = Phase([self.match1, self.match2])
    
    def noMatches(self):
        """ Test that the phase is not completable when no matches are provided """
        assert not self.phase.completable({self.match1:[]}), "Phase should not be completable if all matches are not included"
    
    def notEnoughMatches(self):
        """ Test that the phase is not completable when not all matches are accounted for """
        assert not self.phase.completable({self.match1:[]}), "Phase should not be completable if all matches are not included"
        
    def unmatchedMatches(self):
        """ Test that the phase is not completable when neither match is finished """
        assert not self.phase.completable({self.match1:[], self.match2:[]}), "Phase should not be completable if all matches are not matched"
        
    def notAllMatchesMatched(self):
        """ Test that the phase is not completable when not all matches are finished """
        assert not self.phase.completable({self.match1:[], self.match2:[NumberCard(1, None)]}), "Phase should not be completable if all matches are not matched"
        
    def allMatchesMatched(self):
        """ Test that the phase is not completable when not all matches are finished """
        assert self.phase.completable({self.match1:[NumberCard(2, None)], self.match2:[NumberCard(1, None)]}), "Phase should be completable if all matches are matched"

# Collect all test cases in this class
testcasesCompletable = ["noMatches", "notEnoughMatches", "unmatchedMatches", "notAllMatchesMatched", "allMatchesMatched"]
suiteCompletable = unittest.TestSuite(map(completable, testcasesCompletable))

##########################################################

# Collect all test cases in this file
suites = [suiteCompletable]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
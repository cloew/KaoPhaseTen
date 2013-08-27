from Game.Card.number_card import NumberCard
from Game.Phase.Match.number_set import NumberSet

import unittest

class matched(unittest.TestCase):
    """ Test cases of matched """
    
    def  setUp(self):
        """ Build the Number Set for the test """
        self.numberSet = NumberSet(3)
        
    def noCards(self):
        """ Test that no cards returns False """
        assert not self.numberSet.matched([]), "Assert there is no match when no cards are given."
    
    def notEnoughCards(self):
        """ Test that no cards returns False """
        assert not self.numberSet.matched([self.getNumberCard()]), "Assert there is no match when not enough cards are given."
        
    def differentNumberCards(self):
        """ Test that no cards returns False """
        assert not self.numberSet.matched([self.getNumberCard(), self.getNumberCard(), self.getNumberCard(2)]), "Assert there is no match when there are enough cards, but of different numbers."
        
    def match(self):
        """ Test that no cards returns False """
        assert self.numberSet.matched([self.getNumberCard(), self.getNumberCard(), self.getNumberCard()]), "Assert there is a match when there are enough cards of the same number."
        
    def moreThanEnoughCards(self):
        """ Test that more than enough cards returns True """
        assert self.numberSet.matched([self.getNumberCard(), self.getNumberCard(), self.getNumberCard(), self.getNumberCard()]), "Assert there is a match when more than enough cards are given."
        
    def getNumberCard(self, number=1):
        """ Returns a Number Card """
        return NumberCard(number, None)

# Collect all test cases in this class
testcasesMatched = ["noCards", "notEnoughCards", "differentNumberCards", "match", "moreThanEnoughCards"]
suiteMatched = unittest.TestSuite(map(matched, testcasesMatched))

##########################################################

# Collect all test cases in this file
suites = [suiteMatched]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
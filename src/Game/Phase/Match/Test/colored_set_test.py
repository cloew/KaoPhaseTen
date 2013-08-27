from Game.globals import BLUE, GREEN, RED, YELLOW
from Game.Card.number_card import NumberCard
from Game.Phase.Match.colored_set import ColoredSet

import unittest

class matched(unittest.TestCase):
    """ Test cases of matched """
    
    def  setUp(self):
        """ Build the Number Set for the test """
        self.colorSet = ColoredSet(3)
        
    def noCards(self):
        """ Test that no cards returns False """
        assert not self.colorSet.matched([]), "Assert there is no match when no cards are given."
    
    def notEnoughCards(self):
        """ Test that no cards returns False """
        assert not self.colorSet.matched([self.getNumberCard()]), "Assert there is no match when not enough cards are given."
        
    def differentNumberCards(self):
        """ Test that no cards returns False """
        assert not self.colorSet.matched([self.getNumberCard(), self.getNumberCard(), self.getNumberCard(RED)]), "Assert there is no match when there are enough cards, but of different colors."
        
    def match(self):
        """ Test that no cards returns False """
        assert self.colorSet.matched([self.getNumberCard(), self.getNumberCard(), self.getNumberCard()]), "Assert there is a match when there are enough cards of the same color."
        
    def moreThanEnoughCards(self):
        """ Test that more than enough cards returns True """
        assert self.colorSet.matched([self.getNumberCard(), self.getNumberCard(), self.getNumberCard(), self.getNumberCard()]), "Assert there is a match when more than enough cards are given."
        
    def getNumberCard(self, color=BLUE):
        """ Returns a Number Card """
        return NumberCard(1, color)

# Collect all test cases in this class
testcasesMatched = ["noCards", "notEnoughCards", "differentNumberCards", "match", "moreThanEnoughCards"]
suiteMatched = unittest.TestSuite(map(matched, testcasesMatched))

##########################################################

# Collect all test cases in this file
suites = [suiteMatched]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
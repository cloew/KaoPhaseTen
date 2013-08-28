from Game.Card.number_card import NumberCard
from Game.Card.wild_card import WildCard
from Game.Phase.Match.run import Run

import unittest

class matched(unittest.TestCase):
    """ Test cases of matched """
    
    def  setUp(self):
        """ Build the Number Set for the test """
        self.run = Run(3)
        
    def noCards(self):
        """ Test that no cards returns False """
        assert not self.run.matched([]), "Assert there is no match when no cards are given."
    
    def notEnoughCards(self):
        """ Test that no cards returns False """
        assert not self.run.matched([self.getNumberCard(), self.getNumberCard(2)]), "Assert there is no match when not enough cards are given."
        
    def gap(self):
        """ Test that a sequence with a gap returns False """
        assert not self.run.matched([self.getNumberCard(1), self.getNumberCard(2), self.getNumberCard(4)]), "Assert there is no match when there are enough cards, but of different numbers."
        
    def match(self):
        """ Test that no cards returns False """
        assert self.run.matched([self.getNumberCard(), self.getNumberCard(2), self.getNumberCard(3)]), "Assert there is a match when there are enough cards of the same number."
        
    def moreThanEnoughCards(self):
        """ Test that more than enough cards returns True """
        assert self.run.matched([self.getNumberCard(1), self.getNumberCard(2), self.getNumberCard(3), self.getNumberCard(4)]), "Assert there is a match when more than enough cards are given."
    
    def wildAtBeginning(self):
        """ Test that a wild can match at the beginning """
        assert self.run.matched([WildCard(), self.getNumberCard(2), self.getNumberCard(3)]), "Assert there is a match when a wild is used at the beginning."
    
    def wildInMiddle(self):
        """ Test that a wild can match in the middle """
        assert self.run.matched([self.getNumberCard(1), WildCard(), self.getNumberCard(3)]), "Assert there is a match when a wild is used in the middle."
        
    def wildAtEnd(self):
        """ Test that a wild can match at the end """
        assert self.run.matched([self.getNumberCard(1), self.getNumberCard(2), WildCard()]), "Assert there is a match when a wild is used at the end."
        
    def wildReplaced(self):
        """ Test that replacing a wild cannot match """
        wildCard = WildCard()
        assert self.run.matched([self.getNumberCard(1), self.getNumberCard(2), wildCard]), "Assert there is a match when a wild is used at the end."
        assert self.run.matched([self.getNumberCard(1), self.getNumberCard(2), self.getNumberCard(3), wildCard]), "Assert there is a match when a wild is replaced."
        
    def wildReplacedStored(self):
        """ Test that replacing a wild cannot match when the value is stored """
        wildCard = WildCard()
        assert self.run.matched([self.getNumberCard(1), self.getNumberCard(2), wildCard], store=True), "Assert there is a match when a wild is used at the end."
        assert not self.run.matched([self.getNumberCard(1), self.getNumberCard(2), self.getNumberCard(3), wildCard]), "Assert there is no match when a wild is replaced and the value stored."
        
    def getNumberCard(self, number=1):
        """ Returns a Number Card """
        return NumberCard(number, None)

# Collect all test cases in this class
testcasesMatched = ["noCards", "notEnoughCards", "gap", "match", "moreThanEnoughCards", "wildInMiddle", "wildAtEnd", "wildReplaced", "wildReplacedStored"]
suiteMatched = unittest.TestSuite(map(matched, testcasesMatched))

##########################################################

# Collect all test cases in this file
suites = [suiteMatched]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
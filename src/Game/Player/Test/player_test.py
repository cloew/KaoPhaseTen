from Game.Card.number_card import NumberCard
from Game.Phase.phase import Phase
from Game.Phase.phase_list import PhaseList
from Game.Phase.Match.number_set import NumberSet
from Game.Player.player import Player

import unittest

class completePhase(unittest.TestCase):
    """ Test cases of completePhase """
    
    def  setUp(self):
        """ Build the Player and Phase List for the test """
        self.match1 = NumberSet(1)
        self.match2 = NumberSet(1)
        self.phase1 = Phase([self.match1, self.match2])
        self.phase2 = Phase([])
        self.phaseList = PhaseList([self.phase1, self.phase2])
        self.player = Player(self.phaseList)
        
        self.player.hand = [NumberCard(1, None), NumberCard(2, None)]
        self.matches = {self.match1:[self.player.hand[0]],
                        self.match2:[self.player.hand[1]]}
        
    def nextPhase(self):
        """ Test that the player is now on the next phase """
        self.player.completePhase(self.matches)
        assert self.player.phase == self.phase2, "Player should now be on the next phase"
        
    def cardsRemoved(self):
        """ Test that the cards used to complete the phase are removed from the player's hand """
        self.player.completePhase(self.matches)
        assert self.player.hand == [], "Cards used to match the phase should be removed from the player's hand"

# Collect all test cases in this class
testcasesCompletePhase = ["nextPhase", "cardsRemoved"]
suiteCompletePhase = unittest.TestSuite(map(completePhase, testcasesCompletePhase))

##########################################################

# Collect all test cases in this file
suites = [suiteCompletePhase]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
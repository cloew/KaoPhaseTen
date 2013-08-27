from Game.round import Round
from Game.Phase.standard_phase_list import StandardPhaseList
from Game.Player.player import Player

import unittest

class over(unittest.TestCase):
    """ Test cases of over """
    
    def  setUp(self):
        """ Build the Round and Players for the test """
        self.player1 = Player("", StandardPhaseList)
        self.player2 = Player("", StandardPhaseList)
        self.round = Round([self.player1, self.player2])
        
        self.player1 = self.round.players[0]
        self.player2 = self.round.players[1]
        
    def playersWithHands(self):
        """ Test that when the players have cards in their hands the round is not over """
        self.player1.hand = [None]
        self.player2.hand = [None]
        assert not self.round.over, "Round should not be over when both players have hands"
        
    def onePlayerHasNoHand(self):
        """ Test that when a player has no hand the round is over """
        self.player1.hand = []
        self.player2.hand = [None]
        assert self.round.over, "Round should be over when a player has no hand"
        
    def neitherPlayerHasHand(self):
        """ Test that when neither player has a hand the round is over """
        self.player1.hand = []
        self.player2.hand = []
        assert self.round.over, "Round should be over when neither player has a hand"

# Collect all test cases in this class
testcasesOver = ["playersWithHands", "onePlayerHasNoHand", "neitherPlayerHasHand"]
suiteOver = unittest.TestSuite(map(over, testcasesOver))

##########################################################

# Collect all test cases in this file
suites = [suiteOver]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
from Game.game_deck import GameDeck
from Game.match_pile_manager import MatchPileManager
from Game.Card.number_card import NumberCard
from Game.Phase.phase import Phase
from Game.Phase.phase_list import PhaseList
from Game.Phase.Match.number_set import NumberSet
from Game.Player.player import Player
from Game.Player.player_round_wrapper import PlayerRoundWrapper

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
        self.player = Player("", self.phaseList)
        self.matchPileManager = MatchPileManager()
        self.hand = [NumberCard(1, None), NumberCard(2, None)]
        self.playerRoundWrapper = PlayerRoundWrapper(self.player, self.hand, self.matchPileManager)
        self.matches = {self.match1:[self.hand[0]],
                        self.match2:[self.hand[1]]}
        
    def nextPhase(self):
        """ Test that the player is now on the next phase """
        self.playerRoundWrapper.completePhase(self.matches)
        assert self.playerRoundWrapper.player.phase == self.phase2, "Player should now be on the next phase"
        
    def cardsRemoved(self):
        """ Test that the cards used to complete the phase are removed from the player's hand """
        self.playerRoundWrapper.completePhase(self.matches)
        assert self.playerRoundWrapper.hand == [], "Cards used to match the phase should be removed from the player's hand"
    
    def pileAdded(self):
        """ Test that the cards used to complete the phase are added to a Match Pile """
        self.playerRoundWrapper.completePhase(self.matches)
        for match in self.matches:
            for pile in self.matchPileManager.piles:
                if pile.match is match:
                    assert pile.cards == self.matches[match], "Each match of the phase should have a pile with the cards used to complete it"

# Collect all test cases in this class
testcasesCompletePhase = ["nextPhase", "cardsRemoved", "pileAdded"]
suiteCompletePhase = unittest.TestSuite(map(completePhase, testcasesCompletePhase))

##########################################################

class discard(unittest.TestCase):
    """ Test cases of discard """
    
    def  setUp(self):
        """ Build the Player Wrapper and Deck for the test """
        """ Build the Player and Phase List for the test """
        self.deck = GameDeck()
        self.match1 = NumberSet(1)
        self.match2 = NumberSet(1)
        self.phase1 = Phase([self.match1, self.match2])
        self.phase2 = Phase([])
        self.phaseList = PhaseList([self.phase1, self.phase2])
        self.player = Player("", self.phaseList)
        self.matchPileManager = MatchPileManager()
        self.hand = [NumberCard(1, None), NumberCard(2, None)]
        self.playerRoundWrapper = PlayerRoundWrapper(self.player, list(self.hand), self.matchPileManager)
        
    def cardInDiscard(self):
        """ Test that the card ends up in the discard pile """
        self.playerRoundWrapper.discard(self.hand[0], self.deck)
        assert self.deck.topOfDiscardPile() is self.hand[0], "Card should be at the top of the Discard Pile"
        
    def cardRemoved(self):
        """ Test that the card is removed from the players hand """
        self.playerRoundWrapper.discard(self.hand[0], self.deck)
        assert not self.hand[0] in self.playerRoundWrapper.hand, "Card should not be in the Player's hand"

# Collect all test cases in this class
testcasesDiscard = ["cardInDiscard", "cardRemoved"]
suiteDiscard = unittest.TestSuite(map(discard, testcasesDiscard))

##########################################################

class canPlay(unittest.TestCase):
    """ Test cases of canPlay """
    
    def  setUp(self):
        """ Build the Player Round Wrapper for the test """
        self.match1 = NumberSet(1)
        self.match2 = NumberSet(1)
        self.phase1 = Phase([self.match1, self.match2])
        self.phase2 = Phase([])
        self.phaseList = PhaseList([self.phase1, self.phase2])
        self.player = Player("", self.phaseList)
        self.matchPileManager = MatchPileManager()
        self.hand = [NumberCard(1, None), NumberCard(2, None)]
        self.playerRoundWrapper = PlayerRoundWrapper(self.player, self.hand, self.matchPileManager)
        
    def canPlay_NotSkipped(self):
        """ Test that canPlay works when the Player is not Skipped """
        assert not self.playerRoundWrapper.skipped, "Player should not be skipped"
        assert self.playerRoundWrapper.canPlay(), "Player should be able to play when they are not skipped"
        
    def canPlay_Skipped(self):
        """ Test that canPlay works when the Player is Skipped """
        self.playerRoundWrapper.skipped = True
        assert self.playerRoundWrapper.skipped, "Player should be skipped"
        assert not self.playerRoundWrapper.canPlay(), "Player should not be able to play when they are skipped"
        assert not self.playerRoundWrapper.skipped, "Player should not be skipped anymore"

# Collect all test cases in this class
testcasesCanPlay = ["canPlay_NotSkipped", "canPlay_Skipped"]
suiteCanPlay = unittest.TestSuite(map(canPlay, testcasesCanPlay))

##########################################################

# Collect all test cases in this file
suites = [suiteCompletePhase,
          suiteDiscard,
          suiteCanPlay]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()
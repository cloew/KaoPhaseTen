from Game.match_pile import MatchPile

class PlayerRoundWrapper:
    """ Wrapper for the player for a round of the game """
    
    def __init__(self, player, hand, matchPileManager):
        """ Initialize the Player Round Wrapper """
        self.player = player
        self.hand = hand
        self.matchPileManager = matchPileManager
        
    def addToHand(self, cards):
        """ Adds the given cards to the player's hand """
        self.hand += cards
        
    def completePhase(self, matchesAndCards):
        """ Completes the Player's current phase """
        for match in matchesAndCards:
            cards = matchesAndCards[match]
            pile = MatchPile(match, cards)
            self.matchPileManager.addPile(pile)
            for card in cards:
                self.hand.remove(card)
        
        self.player.completePhase()
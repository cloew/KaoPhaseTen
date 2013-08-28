from Game.match_pile import MatchPile

class PlayerRoundWrapper:
    """ Wrapper for the player for a round of the game """
    
    def __init__(self, player, hand, matchPileManager):
        """ Initialize the Player Round Wrapper """
        self.player = player
        self.hand = hand
        self.matchPileManager = matchPileManager
        self.phaseCompleted = False
        self.hand.sort()
    
    @property
    def phase(self):
        """ Return the player's phase """
        return self.player.phase
        
    def addToHand(self, cards):
        """ Adds the given cards to the player's hand """
        self.hand += cards
        self.hand.sort()
        
    def discard(self, card, deck):
        """ Discard a card from the player's hand into the deck """
        self.hand.remove(card)
        deck.discard(card)
        
    def hit(self, matchPile, card):
        """ Hit a card on a match pile """
        matchPile.add(card)
        self.hand.remove(card)
        
    def completePhase(self, matchesAndCards):
        """ Completes the Player's current phase """
        self.phaseCompleted = True
        
        for match in matchesAndCards:
            cards = matchesAndCards[match]
            pile = MatchPile(match, cards)
            self.matchPileManager.addPile(pile)
            for card in cards:
                self.hand.remove(card)
        
        self.player.completePhase()
        
    def __repr__(self):
        """ Return the string representation of the Player """
        return str(self.player)
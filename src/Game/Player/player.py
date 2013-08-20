
class Player:
    """ Represents a Player """
    
    def __init__(self, phaseList):
        """ Initialize the Player """
        self.hand = []
        self.phaseList = phaseList
        self.phase = phaseList.startingPhase
    
    def addToHand(self, cards):
        """ Adds the given cards to the player's hand """
        self.hand += cards
        
    def completePhase(self, matchesAndCards):
        """ Completes the Player's current phase """
        for match in matchesAndCards:
            for card in matchesAndCards[match]:
                self.hand.remove(card)
                
        self.phase = self.phaseList.nextPhase(self.phase)
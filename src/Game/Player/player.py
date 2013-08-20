
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
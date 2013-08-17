
class Phase:
    """ Represents a Phase """
    
    def __init__(self, matches):
        """ Initialize the Phase with the matches that must be made """
        self.matches = matches
        
    def completable(self, matchesAndCards):
        """ Return if the cards and matches can complete the phase """
        if set(self.matches) != set(matchesAndCards.keys()):
            return False
            
        for match in matchesAndCards:
            if not match.matched(matchesAndCards[match]):
                return False
        else:
            return True 
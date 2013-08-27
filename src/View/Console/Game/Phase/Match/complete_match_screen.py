
class CompleteMatchScreen:
    """ Represents the view for Completing a Match """
    
    def __init__(self, match, availableCards, matchesToCards):
        """ Initialize the view """
        self.match = match
        self.availableCards = availableCards
        self.matchesToCards = matchesToCards
        
    def draw(self):
        """ Draw the Screen """
        print "{0} -- {1}\r".format(self.match, self.match.matched(self.matchesToCards[self.match]))
        print "{0}\r".format(self.matchesToCards[self.match])
        print "\r"
        print "Add a Card to the match\r"
        
        characters = ['1','2','3','4','5','6','7','8','9','0','-']
        for i in range(len(self.availableCards)):
            print "{0}: {1}\r".format(characters[i], self.availableCards[i])
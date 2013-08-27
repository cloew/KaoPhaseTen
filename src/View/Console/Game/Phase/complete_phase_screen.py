from View.Console.Game.Card.card_list_view import CardListView

class CompletePhaseScreen:
    """ Screen for a player to try and complete their phase """
    
    def __init__(self, player, availableCards, matchesToCards):
        """ Initialize the Screen """
        self.player = player
        self.availableCards = availableCards
        self.matchesToCards = matchesToCards
        
    def draw(self):
        """ Draw he Screen """
        print "Phase Complete: {0}\r".format(self.player.phase.completable(self.matchesToCards))
        
        if self.player.phase.completable(self.matchesToCards):
            print "c. Complete Phase"
            print "\r"
        
        for match in self.matchesToCards:
            print "{0}: {1} -- {2}\r".format(match, CardListView(self.matchesToCards[match]).draw(), match.matched(self.matchesToCards[match]))
            
        print "\r"
        print "1. Give Up\r"
        index = 2
        for match in self.matchesToCards:
            print "{0}. Try to complete {1}\r".format(index, match)
            index += 1
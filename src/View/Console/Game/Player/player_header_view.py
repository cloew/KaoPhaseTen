from View.Console.Game.hand_view import HandView
from View.Console.Game.match_pile_view import MatchPileView
from View.Console.Game.Card.card_view_factory import GetCardView
from View.Console.Game.Phase.phase_view import PhaseView

from kao_gui.console.console_widget import ConsoleWidget

class PlayerHeaderView(ConsoleWidget):
    """ Represents the view for a Player Standard Information """
    
    def __init__(self, player, gameDeck, matchPileManager):
        """ Initialize the view """
        self.player = player
        self.gameDeck = gameDeck
        self.phaseView = PhaseView(player.phase)
        self.handView = HandView(player)
        self.matchPileView = MatchPileView(matchPileManager)
        
    def draw(self):
        """ Draw the Widget """
        print "{0}'s Turn\r".format(self.player)
        print "\r"
        self.phaseView.draw()
        print "\r"
        self.matchPileView.draw()
        print "\r"
        card = self.gameDeck.peekAtDiscardPile()
        if card is None:
            discardString = "Empty"
        else:
            discardString = GetCardView(card).draw()
        print "Top of Discard: {0}\r".format(discardString)
        print "\r"
        self.handView.draw()
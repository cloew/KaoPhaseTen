from View.Console.Game.Player.player_header_view import PlayerHeaderView
from match_pile_view import MatchPileView

class PlayerTurnScreen:
    """ Represents the screen for a player turn """
    
    def __init__(self, player, deck, matchPileManager):
        """ Initialize the Screen """
        self.player = player
        self.headerView = PlayerHeaderView(player, deck, matchPileManager)
    
    def draw(self):
        """ Draw the Round Screen """
        self.headerView.draw()
        
        if self.player.phaseCompleted:
            print "1: Try to hit a match pile.\r"
        else:
            print "1: Try to complete the phase.\r"
        print "2: Discard and end turn.\r"
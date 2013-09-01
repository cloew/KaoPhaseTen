from kao_gui.console.console_widget import ConsoleWidget

class SkipScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, players):
        """ Initialize the view """
        self.players = players
        if len(self.players) > 0:
            self.selected = players[0]
        else:
            self.selected = None
        
    def draw(self):
        """ Draw the Widget """
        for player in self.players:
            if player is self.selected:
                header = "-->"
            else:
                header = "   "
            print "{0} {1}\r".format(header, player)
            
    def selectNextPlayer(self):
        """ Select the Next Player, if possible """
        index = self.players.index(self.selected)
        index += 1
        if index < len(self.players):
            self.selected = self.players[index]
            
    def selectPreviousPlayer(self):
        """ Select the Previous Player, if possible """
        index = self.players.index(self.selected)
        index -= 1
        if index >= 0:
            self.selected = self.players[index]
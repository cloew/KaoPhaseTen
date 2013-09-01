from kao_gui.console.console_widget import ConsoleWidget

class SkipScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, players):
        """ Initialize the view """
        self.players = players
        
    def draw(self):
        """ Draw the Widget """
        print self.players
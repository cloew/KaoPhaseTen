from kao_gui.console.console_widget import ConsoleWidget

class PlayerNameScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self):
        """ Initialize the view """
        self.name = ""
        
    def draw(self):
        """ Draw the Widget """
        print "Enter Player Name.\r"
        print "{0}\r".format(self.name)
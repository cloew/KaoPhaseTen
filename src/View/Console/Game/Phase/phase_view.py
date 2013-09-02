from kao_gui.console.console_widget import ConsoleWidget

class PhaseView(ConsoleWidget):
    """ Represents the view for a Phase """
    
    def __init__(self, phase):
        """ Initialize the view """
        self.phase = phase
        
    def draw(self):
        """ Draw the Widget """
        print "Current Phase\r"
        for match in self.phase.matches:
            print "{0}\r".format(match)
from kao_gui.console.console_widget import ConsoleWidget

class WildCardView(ConsoleWidget):
    """ Represents the view for a Wild Card """
    
    def __init__(self, card):
        """ Initialize the view """
        self.card = card
        
    def draw(self):
        """ Draw the Widget """
        return "W"
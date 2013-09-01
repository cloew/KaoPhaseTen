from kao_gui.console.console_widget import ConsoleWidget

class StandardCardView(ConsoleWidget):
    """ Represents the view for a standard card """
    
    def __init__(self, card):
        """ Initialize the view """
        self.card = card
        
    def draw(self):
        """ Draw the Widget """
        return str(card)
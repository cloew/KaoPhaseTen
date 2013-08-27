from Game.globals import BLUE, GREEN, RED, YELLOW

from kao_gui.console.console_widget import ConsoleWidget

class CardView(ConsoleWidget):
    """ Represents the view for a Card """
    
    def __init__(self, card):
        """ Initialize the view """
        self.card = card
        
    def draw(self):
        """ Draw the Widget """
        return self.formatTerminalString(self.getColorString()+str(self.card.number)+"{t.normal}")
        
    def getColorString(self):
        """ Return the color string for the given card """
        colorDictionary = {BLUE:"{t.blue}",
                           GREEN:"{t.green}",
                           RED:"{t.red}",
                           YELLOW:"{t.yellow}"}
        if self.card.color in colorDictionary:
            return colorDictionary[self.card.color]
        else:
            return ""
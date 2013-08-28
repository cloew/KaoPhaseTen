from View.Console.Game.Setup.player_name_screen import PlayerNameScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

import string

class PlayerNameController(ConsoleController):
    """ Controller for choosing a Player Name """
    
    def __init__(self):
        """ Initialize the *** Controller """
        screen = PlayerNameScreen()
        ConsoleController.__init__(self, screen)
        self.index = 0
        self.addCommands(string.printable, self.addCharacterToName)
        self.addCommand(ENDL, self.stopRunning)
        
    def addCharacterToName(self, event):
        """ Add Character to the name """
        self.screen.name += event
        
    @property
    def name(self):
        """ Return the Name """
        return self.screen.name
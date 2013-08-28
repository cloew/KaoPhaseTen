from View.Console.Game.Setup.game_setup_screen import GameSetupScreen

from kao_gui.console.console_controller import ConsoleController

class GameSetupController(ConsoleController):
    """ Controller for Game Setup """
    
    def __init__(self):
        """ Initialize the Game Setup Controller """
        screen = GameSetupScreen()
        ConsoleController.__init__(self, screen, commands={'1':self.setPlayerCount,
                                                           '2':self.setPlayerCount,
                                                           '3':self.setPlayerCount,
                                                           '4':self.setPlayerCount,
                                                           '5':self.setPlayerCount,
                                                           '6':self.setPlayerCount})
        
    def setPlayerCount(self, event):
        """ Set the player Count """
        self.playerCount = int(event)
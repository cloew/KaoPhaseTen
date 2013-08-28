from View.Console.Game.Setup.game_setup_controller import GameSetupController
from View.Console.Game.game_controller import GameController
from kao_gui.console.window import Window

import sys

def main(args):
    """ Run the main file """
    controller = GameSetupController()
    controller.run()
    
    if controller.playerCount > 0:
        game_controller = GameController(controller.playerCount, controller.names)
        game_controller.run()
        Window.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])
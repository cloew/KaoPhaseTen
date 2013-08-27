from View.Console.Game.game_controller import GameController
from kao_gui.console.window import Window

import sys

def main(args):
    """ Run the main file """
    game_controller = GameController(1)
    game_controller.run()
    Window.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])
from Game.game import Game

from View.Console.Game.round_controller import RoundController
from kao_gui.console.window import Window

import sys

def main(args):
    """ Run the main file """
    game = Game(1)
    round_controller = RoundController(game.getNewRound())
    
    round_controller.run()
    Window.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])
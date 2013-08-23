from Game.round import Round
from Game.Phase.standard_phase_list import StandardPhaseList
from Game.Player.player import Player

from View.Console.Game.round_controller import RoundController
from kao_gui.console.window import Window

import sys

def main(args):
    """ Run the main file """
    player = Player(StandardPhaseList)
    round_controller = RoundController([player])
    
    round_controller.run()
    Window.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])
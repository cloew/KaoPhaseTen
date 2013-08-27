from View.Console.Game.Phase.complete_phase_screen import CompletePhaseScreen

from kao_gui.console.console_controller import ConsoleController

class CompletePhaseController(ConsoleController):
    """ Controller for letting a player complete a phase """
    
    def __init__(self, player):
        """ Initialize the Controller """
        self.player = player
        self.availableCards = list(self.player.hand)
        self.matchesToCards = {}
        for match in self.player.phase.matches:
            self.matchesToCards[match] = []
        
        self.screen = CompletePhaseScreen(self.player, self.availableCards, self.matchesToCards)
        ConsoleController.__init__(self, self.screen, commands={'1':self.stopRunning})
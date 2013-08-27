from View.Console.Game.Phase.complete_phase_screen import CompletePhaseScreen
from View.Console.Game.Phase.Match.complete_match_controller import CompleteMatchController

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
        ConsoleController.__init__(self, self.screen, commands={'1':self.stopRunning,
                                                                '2':self.tryToCompleteMatch,
                                                                '3':self.tryToCompleteMatch,
                                                                'c':self.completePhase})
        
    def tryToCompleteMatch(self, event):
        """ Try to Complete a Match """
        items = ['2', '3']
        if event in items:
            index = items.index(event)
            controller = CompleteMatchController(self.matchesToCards.keys()[index], self.availableCards, self.matchesToCards)
            controller.run()
            
    def completePhase(self, event):
        """ Complete the Phase, if actually possible """
        if self.player.phase.completable(self.matchesToCards):
            self.player.completePhase(self.matchesToCards)
            self.stopRunning()
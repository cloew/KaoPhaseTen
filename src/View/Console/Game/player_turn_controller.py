from View.Console.Game.player_turn_screen import PlayerTurnScreen
from View.Console.Game.Phase.complete_phase_controller import CompletePhaseController
from View.Console.Game.Player.discard_controller import DiscardController
from View.Console.Game.Player.hit_controller import HitController

from kao_gui.console.console_controller import ConsoleController

class PlayerTurnController(ConsoleController):
    """ Controller for a single player's turn """
    
    def __init__(self, player, matchPileManager, deck):
        """ Initialize the Player Turn Controller """
        self.player = player
        self.matchPileManager = matchPileManager
        self.deck = deck
        screen = PlayerTurnScreen(self.player, deck, self.matchPileManager)
        ConsoleController.__init__(self, screen, commands={'1':self.doRelevantAction,
                                                           '2':self.discardACard})
        
        
    def doRelevantAction(self, event):
        """ Do action depending on whether a player has completed their phase """
        if self.player.phaseCompleted:
            self.tryToHit()
        else:
            self.tryToCompletePhase()
    
    def tryToCompletePhase(self):
        """ Let the player try to complete their phase """
        controller = CompletePhaseController(self.player)
        controller.run()
        
    def tryToHit(self):
        """ Let the player try to hit a match pile """
        controller = HitController(self.player, self.matchPileManager)
        controller.run()
        
    def discardACard(self, event):
        """ Discard a card from the player's hand """
        controller = DiscardController(self.player, self.deck)
        controller.run()
        self.stopRunning()
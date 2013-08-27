from View.Console.Game.player_turn_screen import PlayerTurnScreen

from kao_gui.console.console_controller import ConsoleController

class PlayerTurnController(ConsoleController):
    """ Controller for a single player's turn """
    
    def __init__(self, player, matchPileManager, deck):
        """ Initialize the Player Turn Controller """
        self.player = player
        self.matchPileManager = matchPileManager
        self.deck = deck
        screen = PlayerTurnScreen(self.player, self.matchPileManager)
        ConsoleController.__init__(self, screen, commands={'1':self.discardACard})
        
    def discardACard(self):
        """ Discard a card from the player's hand """
        card = self.player.hand[0]
        self.player.discard(card, self.deck)
        self.stopRunning()
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
        ConsoleController.__init__(self, screen, commands={'1':self.discardACard,
                                                           '2':self.discardACard,
                                                           '3':self.discardACard,
                                                           '4':self.discardACard,
                                                           '5':self.discardACard,
                                                           '6':self.discardACard,
                                                           '7':self.discardACard,
                                                           '8':self.discardACard,
                                                           '9':self.discardACard,
                                                           '0':self.discardACard,
                                                           '-':self.discardACard})
        
    def discardACard(self, event):
        """ Discard a card from the player's hand """
        items = ['1','2','3','4','5','6','7','8','9','0','-']
        index = items.index(event)
        card = self.player.hand[index]
        self.player.discard(card, self.deck)
        self.stopRunning()
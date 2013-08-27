from View.Console.Game.Player.discard_screen import DiscardScreen

from kao_gui.console.console_controller import ConsoleController

class DiscardController(ConsoleController):
    """ Controller for a player discarding a card from their hand """
    
    def __init__(self, player, deck):
        """ Initialize the Discard Controller """
        self.player = player
        self.deck = deck
        screen = DiscardScreen(self.player)
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
        if event in items:
            index = items.index(event)
            if index < len(self.player.hand):
                card = self.player.hand[index]
                self.player.discard(card, self.deck)
                self.stopRunning()
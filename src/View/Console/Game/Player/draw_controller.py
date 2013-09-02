from View.Console.Game.Player.draw_screen import DrawScreen

from kao_gui.console.console_controller import ConsoleController

class DrawController(ConsoleController):
    """ Controller for having a player draw a card """
    
    def __init__(self, player, gameDeck):
        """ Initialize the Draw Controller """
        self.player = player
        self.gameDeck = gameDeck
        screen = DrawScreen(player, gameDeck)
        ConsoleController.__init__(self, screen, commands={'1':self.drawFromDeck,
                                                           '2':self.drawFromDiscard})
        
    def drawFromDeck(self, event):
        """ Draw a Card from the deck """
        cards = self.gameDeck.draw()
        self.draw(cards)
        
    def drawFromDiscard(self, event):
        """ Draw a Card from the deck """
        if self.gameDeck.canDrawFromDiscard():
            cards = self.gameDeck.drawFromDiscardPile()
            self.draw(cards)
        
    def draw(self, cards):
        """ Draw a Card from the deck """
        self.player.addToHand(cards)
        self.stopRunning()
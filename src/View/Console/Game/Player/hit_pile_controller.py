from View.Console.Game.Player.hit_pile_screen import HitPileScreen

from kao_gui.console.console_controller import ConsoleController

class HitPileController(ConsoleController):
    """ Controller for letting the player actually try to hit a match pile """
    
    def __init__(self, player, matchPile):
        """ Initialize the Controller """
        self.player = player
        self.matchPile = matchPile
        screen = HitPileScreen(player, matchPile)
        ConsoleController.__init__(self, screen, commands={'1':self.tryToHitPile,
                                                           '2':self.tryToHitPile,
                                                           '3':self.tryToHitPile,
                                                           '4':self.tryToHitPile,
                                                           '5':self.tryToHitPile,
                                                           '6':self.tryToHitPile,
                                                           '7':self.tryToHitPile,
                                                           '8':self.tryToHitPile,
                                                           '9':self.tryToHitPile,
                                                           '0':self.tryToHitPile,
                                                           '-':self.tryToHitPile})        
    def tryToHitPile(self, event):  
        """ Try To Hit the pile with the card denoted by the event """
        items = ['1','2','3','4','5','6','7','8','9','0','-']
        if event in items:
            index = items.index(event)
            if index < len(self.player.hand):
                card = self.player.hand[index]
                if self.matchPile.matches(card):
                    self.player.hit(self.matchPile, card)
                    self.stopRunning()
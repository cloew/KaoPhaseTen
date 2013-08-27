from View.Console.Game.Phase.Match.complete_match_screen import CompleteMatchScreen

from kao_gui.console.console_controller import ConsoleController

class CompleteMatchController(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self, match, availableCards, matchesToCards):
        """ Initialize the *** Controller """
        self.match = match
        self.availableCards = availableCards
        self.matchesToCards = matchesToCards
        self.screen = CompleteMatchScreen(match, availableCards, matchesToCards)
        ConsoleController.__init__(self, self.screen, commands={'1':self.addCard,
                                                                '2':self.addCard,
                                                                '3':self.addCard,
                                                                '4':self.addCard,
                                                                '5':self.addCard,
                                                                '6':self.addCard,
                                                                '7':self.addCard,
                                                                '8':self.addCard,
                                                                '9':self.addCard,
                                                                '0':self.addCard,
                                                                '-':self.addCard})
                                                                          
    def addCard(self, event):
        """ Add a Card """
        items = ['1','2','3','4','5','6','7','8','9','0','-']
        if event in items:
            index = items.index(event)
            if index < len(self.availableCards):
                card = self.availableCards[index]
                self.availableCards.remove(card)
                self.matchesToCards[self.match].append(card)
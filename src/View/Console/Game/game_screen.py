
class GameScreen:
    """ Represents the view for a Game """
    
    def __init__(self, game):
        """ Initialize the view """
        self.game = game
        self.message = "Game is beginning with {0} players.".format(len(self.game.players))
        
    def draw(self):
        """ Draw the Screen """
        print "{0}\r".format(self.message)
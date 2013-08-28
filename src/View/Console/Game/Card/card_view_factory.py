from Game.Card.number_card import NumberCard
from Game.Card.wild_card import WildCard

from View.Console.Game.Card.number_card_view import NumberCardView
from View.Console.Game.Card.wild_card_view import WildCardView

def GetCardView(card):
    """ Return the appropriate Card View for the given Card """
    viewClasses = {NumberCard.type:NumberCardView,
                   WildCard.type:WildCardView}
                   
    if card.__class__.type in viewClasses:
        return viewClasses[card.__class__.type](card)
    else:
        return None 
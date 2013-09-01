from Game.Card.number_card import NumberCard
from Game.Card.skip_card import SkipCard
from Game.Card.wild_card import WildCard

from View.Console.Game.Card.number_card_view import NumberCardView
from View.Console.Game.Card.standard_card_view import StandardCardView

def GetCardView(card):
    """ Return the appropriate Card View for the given Card """
    viewClasses = {NumberCard.type:NumberCardView,
                   SkipCard.type:StandardCardView,
                   WildCard.type:StandardCardView}
                   
    if card.__class__.type in viewClasses:
        return viewClasses[card.__class__.type](card)
    else:
        return None 
from Game.Phase.Match.attribute_set import AttributeSet

class NumberSet(AttributeSet):
    """ Represents a number set """
    
    @property
    def comparisonAttribute(self):
        """ Return the attribute of the cards to compare """
        return "number"
            
    def __repr__(self):
        """ Return the String Representation of the Numbered Set """
        return "Numbered Set of {0}".format(self.count)
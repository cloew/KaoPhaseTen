from Game.Phase.Match.attribute_set import AttributeSet

class ColoredSet(AttributeSet):
    """ Represents a colored set """
    
    @property
    def comparisonAttribute(self):
        """ Return the attribute of the cards to compare """
        return "color"
            
    def __repr__(self):
        """ Return the String Representation of the Colored Set """
        return "Colored Set of {0}".format(self.count)
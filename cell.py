class Cell:
    def __init__(self, red = 0, green = 0, blue = 0, surroundingCells = []):

        self._red = red
        self._green = green
        self._blue = blue

    """
    CELL COLOR
    each cell's color is determined by genetics and random chance.
    """

    def get_red(self): # get red value of cell's color (0-255)

        return self._red

    def get_green(self): # get green value of cell's color (0-255)

        return self._green

    def get_blue(self): # get blue value of cell's color (0-255)

        return self._blue

    """
    PASSIVE STATISTICS
    each cell is given passive statistics based on color, genetics, and active statistics.
    """

    """
    ATTACK CATEGORY
    """

    def strength(self): # returns strength value, higher attack chance (1-100) 

        pass

    def perception(self): # returns perception vlaue, higher chance to spot enemies (1-100)

        pass

    """
    DEFEND CATEGORY
    """

    def stealth(self): # returns stealth value, higher chance to not be seen (1-100)

        pass

    def resistance(self): # returns resistance value, higher chance to defend attack (1-100)

        pass

    """
    DECISION CATEGORY
    """

    def intelligence(self): # returns intelligence value, higher chance to make the best choice (1-100)

        pass

    def charisma(self): # returns charisma value, higher chance to make friends (1-100)

        pass

    """
    ACTIVE STATISTICS
    each cell is given active statistics based on genetics and surroundings.
    """

    """
    HAPPINESS AND ANGER
    """

    def happiness(self): # returns happy value, higher chance to make friends (1-100).

        pass

    def anger(self): # returns anger value, higher chance to attack (1-100).

        pass

    """
    FEAR AND FOCUS
    """

    def fear(self): # returns fear value, higher chance to defend (1-100).

        pass

    def focus(self): # returns focus value, higher chance to supress emotional actions (1-100).

        pass

    """
    TRUST AND BETRAYAL
    """

    def trust(self): # returns trust value, higher chance to make friends (1-100).

        pass

    def betrayal(self): # returns betrayal value, higher chance to make enemies (1-100).

        pass





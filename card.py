class Card:

    def __init__(self, color, figure):  # init a new card, taken from deck
        self.color = color
        self.figure = figure

    def __str__(self):  # print card
        return self.figure + ' of ' + self.color

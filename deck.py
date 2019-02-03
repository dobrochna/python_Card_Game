import random
import main_game
import card


class Deck:  # deck for the game

    def __init__(self):  # create new deck and fill it with cards
        self.deck = []
        for color in main_game.colors:
            for figure in main_game.figures:
                self.deck.append(card.Card(color, figure))

    def __str__(self):  # print deck
        deck_str = ''
        for element in self.deck:
            deck_str += '\n' + element.__str__()
        return 'Our deck has: ' + deck_str

    def shuffle_deck(self):  # shuffle deck before game
        random.shuffle(self.deck)

    def deal(self):  # deal card
        single_card = self.deck.pop()
        return single_card

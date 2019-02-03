import main_game


class Hand:  # player and dealer hand

    def __init__(self):  # init empty hand
        self.cards = []
        self.value = 0
        self.aces = 0

    def print_hand(self, num):  # print cards in hand
        hand_str = ''
        for value in range(num):
            hand_str += self.cards[value].__str__() + '\n'
        return hand_str

    def add_card(self, card):  # add cards to hand
        self.cards.append(card)
        self.value += main_game.values[card.figure]
        if card.figure == 'A':
            self.aces += 1

    def if_ace(self):  # check if player has an ace in hand
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

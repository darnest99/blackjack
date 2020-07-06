import random

class Deck:
    def __init__(self):
        self.deck = []
    def build(self):
        self.deck = []
        for i in ['diamonds', 'hearts', 'spades', 'clubs']:
            suit = [[l, i] for l in range(2, 15)]
            for k in suit:
                if k[0] > 11:
                    k[0] = 10
            self.deck += suit
        random.shuffle(self.deck)
    def deal(self):
        card = self.deck.pop()
        return card


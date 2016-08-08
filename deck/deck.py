import itertools, random

class Deck:
    "A standard 52 card deck that keeps track of remaining cards"
    def __init__(self, noshuffle = False):
        # A is 14
        self.cards = list(itertools.product(range(2,15), ['s','h','d','c']))

        if (not(noshuffle)):
            random.shuffle(self.cards)

    def take(self, n):
        "Removes n cards from the deck and returns a list of them"
        out = []
        for i in range(n):
            out.append(self.cards.pop())
        return out

    def shuffle(self):
        "Shuffles the deck"
        random.shuffle(self.cards)


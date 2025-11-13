import random
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['\u2660', '\u2665', '\u2666', '\u2663']  # spades, hearts, diamonds, clubs


class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f'{self.rank} {self.suit}'
    




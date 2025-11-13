from card import *
from deck import *
from hand import *
from collections import Counter

class Checker:
    def __init__(self,hand_object):
        self.hand_object = hand_object
        self.combo = []
    
    def result(self):
        self.combo = []
        for card in self.hand_object.hand:
                self.combo.append(card.suit)
        if all(suit == self.combo[0] for suit in self.combo):
            return "You got flash,6 points"
        
        self.combo = []
        for card in self.hand_object.hand:
            self.combo.append(card.rank)
        c = Counter(self.combo)
        if 4 in c.values():
             return "You got quads,8 points"
        if 3 in c.values() and 2 in c.values():
             return "You got fullhouse,7 points"
        if 3 in c.values():
             return "You got set,4 points"
        if 2 in c.values():
             return "You got pair,2 points"